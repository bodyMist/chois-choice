from rest_framework.views   import APIView
from rest_framework.response import Response
# from .serializer import *
from .models import *
from component import models as component
from component import serializer as componentSerializer

#문자열 파싱용
import re 

# Create your views here.

# 용도와 예산을 추출
# 용도 모든 사양들을 비교하여 최고치의 최소사양과 권장사양을 얻음(이게 기준/시작점이 될 것)
# 시작점에서는 cpu, gpu, memory만 있으므로 
# 용도별?로 Hdd/Ssd, mainboard, cooler, case를 선택
# 예)인터넷 서핑용 - Hdd250GB, Ssd 128gb 이상, mainboard는 cpu 소켓에 맞춰서
# 
class Recommendation(APIView):
  
  def get(self, request, format=None):
    uses_name = request.GET.getlist('uses')     # 용도는 다수 입력이 가능(이름만 넘어옴)
    budget = request.GET.get('budget')
    current_price = 0                           # 현재 견적에서의 총 가격
    use_list = []
    for use in uses_name:
      target = Uses.objects.get(name = use)  # 용도 이름으로 각각 용도 객체 검색
      use_list.append(target)                   # 용도 리스트에 추가
    
    basic_spec = self.getMaxUse(use_list)       # 용도 리스트에 대해 최고치 사양 구하기
    
    least_spec= [basic_spec[0].least_processor, basic_spec[0].least_graphics, basic_spec[0].least_memory]
    #if None in least_spec:
    
    least_spec.extend(self.getBasicComponents(least_spec[0], least_spec[1], least_spec[2]))
    
    least_benchmark = [basic_spec[1],basic_spec[2],basic_spec[3]
    ,basic_spec[4],basic_spec[5],basic_spec[6]]

    print(least_spec)
    for target in least_spec:
      if target is None or target.price is None:
        continue
      current_price += target.price
    serializer = componentSerializer.ComponentSerializer(least_spec, many=True)
    return Response(serializer.data);

  # 용도 기준치를 잡은 후 나머지 부품들도 채우기 위한 함수
  # hdd : 500gb, ssd : 250gb, mainboard : ? , cooler : X, case : 적당히?, power: gpu required_power + 100W
  def getBasicComponents(self, cpu, gpu, memory):
    hdd = component.Component.objects.select_related('hdd')\
      .filter(data_type=5, hdd__capacity="500GB")\
      .exclude(price__isnull=True).order_by('price').first()

    ssd = component.Component.objects.select_related('ssd')\
      .filter(data_type=6, ssd__capacity="240GB")\
      .exclude(price__isnull=True).order_by('price').first()
    
    mainboard = component.Component.objects.select_related('mainboard')\
      .filter(data_type=3, mainboard__socket=cpu.cpu.socket)\
      .exclude(price__isnull=True, mainboard__formfactor__isnull=True)\
      .order_by('price').first()


    gpower = gpu.gpu.required_power
    if gpower is None:
      gpower = 0
    power = component.Component.objects.select_related('power')\
      .filter(data_type=7, power__output__gte=(gpower+100))\
      .exclude(price__isnull=True).order_by('price').first()

    m_formfactor = mainboard.mainboard.formfactor.split(' ')[0]
    p_type = power.power.type.split(' ')[0]

    case = component.Component.objects.select_related('case')\
      .filter(data_type=9, case__depth__gte=(gpu.gpu.width+50))\
      .exclude(price__isnull=True).order_by('price').first()
    
    result = [mainboard, hdd, ssd, power, case]
    return result

  # 더 높은 벤치마크 점수의 부품 이름과 점수를 반환
  # 객체가 없거나 호환성이 맞지 않을 때, 벤치마크 점수가 더 높은 부품을 찾기 위해 사용
  def getHigherBenchmark(self, data_type, score):
    higherBench = BenchMark.objects.filter(data_type=data_type, score__gt=score)\
      .order_by('score').first()
    return higherBench


  # 호환성 체크1
  # cpu, gpu, mainboard 간의 소켓 및 지원 규격 체크
  def checkCompatibility(self, cpu, memory, mainboard):
    result = True
    if cpu.socket != mainboard.socket:
      result = False
    if memory.type in cpu.memory.type:
      result = False
    if mainboard.memory_type != memory.type:
      result = False

    return result

  # 호환성 체크2
  # mainboard, gpu, case, power 간의 폼팩터(크기) 체크
  def checkFormfactor(self, mainboard, gpu, case, power):
    result = True
    m_formfactor = mainboard.formfactor.split(' ')[0]



    return result



  # 입력인자 : 비교할 용도 리스트
  # 출릭인자 : 비교,계산,대입이 끝난 용도 객체 하나, 
  #           해당 객체에 대한 각 {벤치마크 점수와 가격 정보}로 이루어진 리스트
  #           ex) [Uses 객체, 최소cpu 점수 dict, 최소gpu 점수 dict, ...]
  # 출력되는 Uses 객체에는 최소,권장 사양을 만족하는 Component 객체가 들어가있다
  # 기본적으로 벤치마크 점수 기반으로 비교
  # 한쪽이라도 벤치마크 점수가 없을 경우 가격 정보로 비교
  # Memory는 벤치마크까지 끌고와서 비교하기 보다는 capacity만을 비교해서 마지막에
  # capacity 만족하는 최저가 제품 끌고오기
  def getMaxUse(self, uses):
    standard_use = uses[0]
    zero_dictionary = {'benchmark':0, 'price':0}
    # 1번 용도에 대해 benchmark와 가격 얻기
    # 최소사양
    llp = self.getCpuScores(standard_use.least_processor)
    llg = self.getGpuScores(standard_use.least_graphics)
    llm = standard_use.least_memory
    # 권장사양
    # 있다면 점수를 계산하지만, 없다면 0점 dictionary 할당
    lrp = self.getCpuScores(standard_use.rec_processor) \
      if standard_use.rec_processor is not None else zero_dictionary
    lrg = self.getGpuScores(standard_use.rec_graphics) \
      if standard_use.rec_graphics is not None else zero_dictionary
    lrm = standard_use.rec_memory \
      if standard_use.rec_memory is not None else 0

    for i in range(1, len(uses)):
      # 비교대상이 될 용도들에 대해서 benchmark와 가격 가져오기
      rlp = self.getCpuScores(uses[i].least_processor)
      rlg = self.getGpuScores(uses[i].least_graphics)
      rlm = uses[i].least_memory
      rrp = self.getCpuScores(uses[i].rec_processor) \
        if standard_use.rec_processor is not None else zero_dictionary
      rrg = self.getGpuScores(uses[i].rec_graphics) \
        if uses[i].rec_graphics is not None else zero_dictionary
      rrm = uses[i].rec_memory if uses[i].rec_memory is not None else 0

      # 계산 후 대조군과 비교 대입하기
      # 코드 존나 더럽네
      # 최소 사양
      compare = "benchmark"
      if (llp[compare] == 0 or rlp[compare] == 0):
        compare = "price"
      if llp[compare] < rlp[compare]:
        standard_use.least_processor = uses[i].least_processor
        llp = rlp
      compare = "benchmark"
      if (llg[compare] == 0 or rlg[compare] == 0):
        compare = "price"
      if llg[compare] < rlg[compare]:
        standard_use.least_graphics = uses[i].least_graphics
        llg = rlg
      compare = "benchmark"
      if (llm < rlm):
        llm = rlm
      
        # 권장 사양
      if (lrp[compare] == 0 or rrp[compare] == 0):
        compare = "price"
      if lrp[compare] < rrp[compare]:
        standard_use.rec_processor = uses[i].rec_processor
        lrp = rrp
      compare = "benchmark"
      if (lrg[compare] == 0 or rrg[compare] == 0):
        compare = "price"
      if lrg[compare] < rrg[compare]:
        standard_use.rec_graphics = uses[i].rec_graphics
        lrg = rrg
      if (lrm < rrm):
        lrm = rrm
    
    # 용도 테이블의 요구사항 이름을 가지고 있으면 이 함수 이후에 바로 부품을 바꿀수 없기 때문에
    # 특정 Component로 교체해서 반환한다
    standard_use.least_processor = self.getCpuWithUse(standard_use.least_processor)
    standard_use.least_graphics = self.getGpuWithUse(standard_use.least_graphics, llg['benchmark'])
    standard_use.least_memory = self.getMemoryWithUse(llm)
    if standard_use.rec_processor is not None:
      standard_use.rec_processor = self.getCpuWithUse(standard_use.rec_processor)
      standard_use.rec_graphics = self.getGpuWithUse(standard_use.rec_graphics)
      standard_use.rec_memory = self.getMemoryWithUse(lrm)

    
    result = [standard_use, llp, llg, llm, lrp, lrg, lrm]
    return result

  # 입력인자 : 부품명
  # 출력인자 : 입력인자에 대한 가격
  # 부품명을 포함하는 NAME을 가진 부품, price null 제외, 오름차순으로 정렬 후 1번째 반환
  def getComponentPrice(self, component_name):
    price = component.Component.objects.filter(name__icontains=component_name) \
      .only("price").exclude(price__isnull=True).order_by('price').first()

    return price

  #====================CPU BenchMark 점수 가져오기 ↓==================================
  cpu_mapping_before = ['코어','제온','펜티엄','셀러론','애슬론','페넘','스레드리퍼','쿼드','라이젠']
  cpu_mapping_after = ['Core ','Xeon ','Pentium ','Celeron ','Athlon ','Phenom ','TR ',' Quad ', 'Ryzen ']
  
  # 입력인자 : DB의 Component 또는 Uses Cpu name(processor)
  # 출력인자 : benchmark 점수 & 최저가 price 의 dictionary
  # cpu 1개에 대한 과정!
  def getCpuScores(self, row_name):
    mapped_name = self.cpuNameMapping(row_name)
    parsed_name = self.cpuParse(mapped_name)
    benchmark = self.getCpuBenchmark(parsed_name)
    price = self.getComponentPrice(row_name)
    result = {'benchmark':benchmark, 'price':price}
    return result
  
  # 입력인자 : Uses CPU name
  # 용도 테이블의 cpu name에서 영어 명칭을 한글로 매핑
  # 출력인자 : 매핑이 완료된 uses cpu name
  def useToCpuMapping(self, use_name):
    for i in range(len(self.cpu_mapping_before)):
      use_name.replace(self.cpu_mapping_after[i], self.cpu_mapping_before[i])
    return use_name
  
  # 입력인자 : 매핑이 완료된 uses cpu name
  # 검색에 필요한 토큰 구하기
  # 출력인자 : 회사명이 제거되고 split된 uses cpu name 토큰 리스트
  def useCpuParse(self, use_name):
    use_name = re.sub('-', ' ', use_name)   # intel사의 세대와 제품명 사이의 하이픈 제거
    cpu_split = use_name.split(" ")
    del cpu_split[0]    # 회사명 Intel Amd 삭제
    return cpu_split

  # 입력인자 : 용도 테이블의 cpu 이름
  # 토큰 리스트를 이용해서 가격이 가장 낮은 cpu component 반환
  # 출력인자 : 해당되는 cpu component
  def getCpuWithUse(self, use_name):
    cpu_split = self.useCpuParse(use_name)
    result = component.Component.objects.select_related('cpu')\
      .filter(data_type=1)\
      .filter(name__icontains=cpu_split[0])\
      .filter(name__icontains=cpu_split[1])\
      .order_by('price').first()
    return result



  # 입력인자 : DB의 Component 또는 Uses CPU name(processor)
  # 인텔,라이젠,제온 등등 한글을 영어명칭으로 매핑하는 메소드
  # 출력인자 : 매핑이 완료된 cpu name
  def cpuNameMapping(self, row_name):
    for i in range(len(self.cpu_mapping_before)):
      row_name.replace(self.cpu_mapping_before[i], self.cpu_mapping_after[i])
    row_name.replace('  ',' ')  # 띄워쓰기 중복 없애기
    return row_name
  
  # 입력인자 : mapping이 끝난 cpu name
  # 출력인자 : 회사명, 괄호가 제거되고 split된 cpu_name 토큰 리스트
  def cpuParse(self, row_name):
    # delete_target = re.findall('\w+\W\w+세대', row_name)
    # row_name.replace(delete_target, '')
    braket = re.findall('\(\w+\)', row_name)   # 괄호 내용은 필요없으므로 삭제
    for i in braket:
      row_name = row_name.replace(i, '')
    row_name = re.sub("-[0-9]+세대", " ", row_name)  # '-[0-9]+세대' 정보 삭제

    row_name.replace(' or ', ' ')
    row_name.strip()     # 양 끝단 공백 split하기 전에 제거
    cpu_split = row_name.split(' ')
    del cpu_split[0]    # 인텔 / AMD 삭제
    return cpu_split

  # 입력인자 : 회사명, 괄호가 제거되고 split된 cpu_name 토큰 리스트
  # 출력인자 : 특정지어진다면 해당 밴치마크 점수를, 없다면 0을 반환
  def getCpuBenchmark(self, parsed_name):
    # DB에서 시리즈명으로 검색
    benchmark_list = BenchMark.objects.filter(name = parsed_name[0])   
    # 해당 시리즈에 대한 벤치마크를 전부 가져왔으므로 
    # cpu name 토큰들로 일치하는 정보를 검색
    for i in benchmark_list:
      for j in range(1, len(parsed_name)):
        index = i.name.find(parsed_name[j])
        if index != -1:
          return benchmark_list[i].score
    return 0

  #====================GPU BenchMark 점수 가져오기 ↓==================================
  # Component에서는 name - manufacture & [0] 버리기, 
  # 용도 테이블에서는 특정 제품명이나 capacity을 기입 -> capacity로는 검색 불가
  # capacity로 기입되어 있을 경우, component에서 name으로 검색 -> 그 중에서

  def getGpuScores(self, row_name):
    mapped_name = self.gpuMapping(row_name)
    parsed_name = self.gpuParse(mapped_name)
    benchmark = self.getGpuBenchmark(parsed_name)
    price = self.getComponentPrice(row_name)
    result = {'benchmark':benchmark, 'price':price}
    return result

  # super->s , ti -> -ti, xt -> -XT
  # 입력인자 : DB의 Component(data_type=2) 또는 Uses GPU name(graphics)
  # 출력인자 : 일부 명칭이 다시 매핑된 name
  def gpuMapping(self, row_name):
    row_name = row_name.lower()
    row_name.replace("확인중", "")
    row_name.replace(" ti", "-Ti" , 1)
    row_name.replace(" super ", "s ", 1)
    row_name.replace(" xt ", "-XT ", 1)
    if row_name.startswith('gtx'):
      row_name = row_name.replace("gtx", "gtx ") 
    elif row_name.startswith('gt'):
      row_name = row_name.replace("gt", "gt ")
    row_name.replace("  ", " ")
    row_name.strip()
    return row_name
  
  # 입력인자 : 매핑이 완료된 gpu name
  # 출력인자 : 매칭 검색을 하기 위한 parsed_name
  # 예상출력 : GTX 1060-Ti, 
  def gpuParse(self, mapped_name):
    mapped_name = re.sub('[0-9]+GB',"", mapped_name)  # 용도나 gpu_name의 capacity 삭제
    result = mapped_name.split(' ')
    del result[0]
    parsed_name = result[0] + " " + result[1]
    return parsed_name

  # 입력인자 : 매칭 검색이 가능한 parsed name / 시리즈명+제품명 구성 (gtx 1060)
  def getGpuBenchmark(self, parsed_name):
    # icontains를 사용하면 ti버전이나 super 버전, (Mobile)이 딸려올 수 있음
    # 점수 기준으로 내림차순 정렬로 가져오기
    benchmark_list = BenchMark.objects\
      .filter(data_type=2, name__icontains=parsed_name)\
      .order_by('-score')
    
    # 정확하게 일치하는 name이 있을 경우, 해당 벤치 점수를 채택
    # 1060는 3GB 5GB 버전으로 나뉘어서 이에 대한 예외처리로 정규식 파싱교체 사용
    for i in benchmark_list:
      i.name = re.sub('-[0-9]GB', '', i.name)
      if parsed_name == i.name:
        return i.score
    return 0
  
  # 용도의 그래픽 요구사항 이름을 가지고 특정 component를 검색
  # split하고 회사명과 시리즈 명(대분류)을 삭제, 이후 토큰들로 검색
  # 검색할 토큰은 총 3개라고 전제조건을 걸어둔다 (이에 맞게 db 데이터를 넣으라는 뜻)
  # 입력인자 : 용도 테이블의 그래픽 이름
  # 출력인자 : 해당되는 종류의 그래픽 카드 중 최저가 객체 1개
  def getGpuWithUse(self, use_name, score):
    split_name = use_name.split(' ')
    del split_name[0]
    result = component.Component.objects.select_related('gpu')\
      .filter(data_type=2)\
      .filter(name__icontains=split_name[0])\
      .filter(name__icontains=split_name[1])\
      .filter(name__icontains=split_name[2])\
      .exclude(price__isnull=True, gpu__width__isnull=True)\
      .order_by('price').first()
    
    while(True):
      if result is not None:
        break;
      higherBenchmark = self.getHigherBenchmark(2, score)
      benchmark_name = higherBenchmark.name
      score = higherBenchmark.score
      result = self.getGpuWithBenchmark(benchmark_name)


    return result


  def getGpuWithBenchmark(self, benchmark_name):
    benchmark_name = benchmark_name.replace("-", " ")
    benchmark_name = benchmark_name.replace("s "," super ", 1)
    benchmark_name = re.sub('\(\w+\)', '', benchmark_name)    # 괄호 내용 삭제
    name_token = benchmark_name.split(' ')
    #print(benchmark_name)
    result = component.Component.objects.select_related('gpu')\
      .filter(data_type=2)\
      .filter(name__icontains=name_token[0])\
      .filter(name__icontains=name_token[1])\
      .exclude(price__isnull=True, gpu__width__isnull=True)\
      .order_by('price').first()
    return result

  #====================MEMORY BenchMark 점수 가져오기 ↓=============================
  # Memory는 시리즈명(Trident, Fury, Vengeance 등) + 클럭(3200) + 용량(2x8G) 정보로 검색 가능
  # Memory BenchMark 데이터가 굉장히 적음(약 100개)
  # Uses에서는
 
  #==================Uses memory 요구사항으로 BenchMark 점수 가져오기================
  # 용량만 기입되어있는 용도-메모리를 최저금액 제품을 Component에서 하나 가져오기
  def getMemoryWithUse(self, use_capacity):
    result = component.Component.objects.select_related('memory')\
      .filter(data_type=4, memory__capacity__gte=use_capacity, memory__device="데스크탑용")\
      .exclude(price__isnull=True).order_by('price').first()

    return result

  #====================Component name으로 BenchMark 점수 가져오기 ==================
  memory_series = ['Vengeance', 'Trident', 'Ripjaws', 'Dominator', 'Ballistix', 'Predator']


  def getMemoryScores(self, row_name):
    parsed_name = self.memoryParse(row_name)
    benchmark = self.getMemoryBenchmark(parsed_name)
    price = self.getComponentPrice(row_name)
    result = {'benchmark': benchmark, 'price':price}
    return result

  # 입력인자 : DB Component memory name
  # 출력인자 : [DDR, 클럭 , 용량(GB), 시리즈명(공백가능)]
  def memoryParse(self, row_name):
    row_name.replace("-", " ")    # DDR 세대와 클럭 사이의 '-' 하이픈 제거
    bracket = re.findall('\(\d+GB\)', row_name) # memory name에서 제품의 총 capacity 추출 / 단일 갯수 제품일때
    multi_bracket = re.findall('\(\d+Gx.+\)', row_name)  # memory name에서 16Gx2 이런거 추출  / 2개 이상 갯수일때
    row_name.strip()
    
    # 시리즈 명 포함여부 검사하기
    series_name = ""
    for i in range(len(self.memory_series)):
      if self.memory_series[i] in row_name:
        series_name = self.memory_series[i]
        break

    # name에 2개입으로 들어간 제품인지 검사하고 있다면 parsing
    if len(multi_bracket) != 0:   # 내용물이 있다면 이놈을 사용
      bracket = multi_bracket
      bracket = bracket[0].replace('(', '').replace(')','') # findall은 리스트로 반환하기 때문에 0 위치 지정해야함
      bracket = bracket.split('x')   
      bracket_result = bracket[1] + 'x' + bracket[0]

    memory_split = row_name.split(' ')
    del memory_split[0]   # manufacture 제거
    result = [memory_split[0],memory_split[1], bracket_result, series_name]
    return result

  # 입력인자 : parsing 완료된 memory name 토큰 리스트
  # 출력인자 : 내림차순으로 정렬되어 가장 높은 벤치마크 점수
  def getMemoryBenchmark(self, parsed_name):
    benchmark_list= BenchMark.objects\
      .filter(name__icontains=parsed_name[0])\
      .filter(name__icontains=parsed_name[1])\
      .filter(name__icontains=parsed_name[2])\
      .filter(name__icontains=parsed_name[3])\
      .order_by('-score')

    if len(benchmark_list) == 0:
      return 0
    return benchmark_list[0]
