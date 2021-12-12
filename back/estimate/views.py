from rest_framework.views   import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import *
from .serializers import *
from component import models as component
from component import serializer as componentSerializer

#문자열 파싱용, 기능 수행시간 측정용
import re, time

# Create your views here.

# 용도와 예산을 추출
# 용도 모든 사양들을 비교하여 최고치의 최소사양과 권장사양을 얻음(이게 기준/시작점이 될 것)
# 시작점에서는 cpu, gpu, memory만 있으므로 
# 용도별?로 Hdd/Ssd, mainboard, cooler, case를 선택
# 예)인터넷 서핑용 - Hdd250GB, Ssd 128gb 이상, mainboard는 cpu 소켓에 맞춰서
# 
class Recommendation(APIView):
  
  def get(self, request, format=None):
    start = time.time()
    uses_name = request.GET.getlist('uses[]')     # 용도는 다수 입력이 가능(이름만 넘어옴)
    budget = request.GET.get('budget')
    redis_key = "uses_" + ''.join(uses_name) + "_" + "budget_" + budget
    # redis_key 수정할 것
    value = cache.get(redis_key)

    if value is not None:
      serializer = componentSerializer.ComponentSerializer(value, many=True)
      print(time.time() - start)
      return Response(serializer.data)
    least_price = 0                           # 현재 견적에서의 총 가격
    rec_price = 0
    use_list = []
    for use in uses_name:
      target = Uses.objects.get(name = use)  # 용도 이름으로 각각 용도 객체 검색
      use_list.append(target)                   # 용도 리스트에 추가

    basic_spec = self.getMaxUse(use_list)       # 용도 리스트에 대해 최고치 사양 구하기

    # 용도의 사양 조건을 통해 cpu,gpu,memory 기준점을 가져온다
    # cpu,gpu,memory를 기준으로 다른 부품들을 추가한다
    try:
      least_spec= [basic_spec[0].least_processor, basic_spec[0].least_graphics, basic_spec[0].least_memory]
      least_spec.extend(self.getBasicComponents(least_spec[0], least_spec[1], least_spec[2]))
      rec_spec = [basic_spec[0].rec_processor, basic_spec[0].rec_graphics, basic_spec[0].rec_memory]
      rec_spec.extend(self.getBasicComponents(rec_spec[0], rec_spec[1], rec_spec[2]))
    except:
      pass
    least_benchmark = [basic_spec[1],basic_spec[2],basic_spec[3]]
    rec_benchmark = [basic_spec[4],basic_spec[5],basic_spec[6]]
    

    # 최저사양 스펙에 대한 가격 총합
    for target in least_spec:
      if target is None or target.price is None:
        continue
      least_price += target.price

    # 권장사양 스펙에 대한 가격 총합
    for target in rec_spec:
      if target is None or target.price is None:
        continue
      rec_price += target.price
    

    #=============최저 사양이나 그 가격 정보가 없을 경우 0원으로 처리============
    if least_spec[0] is None or least_spec[0].price is None:
      cprice = 0
    else:
      cprice = least_spec[0].price
    if least_spec[1] is None or least_spec[1].price is None:
      gprice = 0
    else:
      gprice = least_spec[1].price
    if least_spec[2] is None or least_spec[2].price is None:
      mprice = 0
    else:
      mprice = least_spec[2].price

    #==============최저 사양 가격 정보와 예산을 비교하여 스펙 업스케일===========
    
    budget = int(budget)    # 사용자가 입력한 예산

    higher_cpu=least_spec[0]
    higher_gpu=least_spec[1]
    higher_memory=least_spec[2]

    while(least_price < budget):
      higher_cpu = self.getExpensiveComponent(1, cprice)
      higher_gpu = self.getExpensiveComponent(2, gprice)
      higher_memory = self.getExpensiveComponent(4, mprice)
      least_price = least_price\
        + higher_cpu.price + higher_gpu.price\
        + higher_memory.price \
        - cprice - gprice - mprice
      cprice = higher_cpu.price
      gprice = higher_gpu.price
      mprice = higher_memory.price


    # 스펙 업스케일 결과의 벤치마크 점수가 최소사양 벤치마크보다 클 때만 덮어쓰기

    control_cpu = self.getCpuScores(higher_cpu.name)
    if higher_gpu is not None:
      control_gpu = self.getGpuScores(higher_gpu.name)
    control_memory = self.getMemoryScores(higher_memory.name)

    # if least_benchmark[0]['benchmark'] < control_cpu['benchmark']:   
    #   if least_benchmark[1]['benchmark'] < control_gpu['benchmark']:  
    #     if least_benchmark[2] < control_memory['price']:
    #       least_spec[0] = higher_cpu
    #       least_spec[1] = higher_gpu
    #       least_spec[2] = higher_memory

    if least_benchmark[0]['benchmark'] < control_cpu['benchmark']:
        least_spec[0] = higher_cpu
    if higher_gpu is not None:
      if least_benchmark[1]['benchmark'] < control_gpu['benchmark']:
          least_spec[1] = higher_gpu  
    if least_benchmark[2] < control_memory['price']:
        least_spec[2] = higher_memory

    # least_spec[0] = higher_cpu
    # least_spec[1] = higher_gpu  
    # least_spec[2] = higher_memory
    if least_spec[1] is None:
      least_spec[1]=component.Component()
    

    #=============권장 사양이나 그 가격 정보가 없을 경우 0원으로 처리============
    if rec_spec[0] is None or rec_spec[0].price is None:
      cprice = 0
    else:
      cprice = rec_spec[0].price
    if rec_spec[1] is None or rec_spec[1].price is None:
      gprice = 0
    else:
      gprice = rec_spec[1].price
    if rec_spec[2] is None or rec_spec[2].price is None:
      mprice = 0
    else:
      mprice = rec_spec[2].price

    #===============권장 사양 가격 정보와 예산을 비교하여 스펙 업스케일링==========
    while(rec_price < budget):
      higher_cpu = self.getExpensiveComponent(1, cprice)
      higher_gpu = self.getExpensiveComponent(2, gprice)
      higher_memory = self.getExpensiveComponent(4, mprice)
      rec_price = rec_price + higher_cpu.price + higher_gpu.price + higher_memory.price- cprice - gprice - mprice
      cprice = higher_cpu.price
      gprice = higher_gpu.price
      mprice = higher_memory.price
    
    # control_group = self.getCpuScores(higher_cpu.name)
    control_cpu = self.getCpuScores(higher_cpu.name)
    if higher_gpu is not None:
      control_gpu = self.getGpuScores(higher_gpu.name)
    control_memory = self.getMemoryScores(higher_memory.name)


    if rec_benchmark[0]['benchmark'] < control_cpu['benchmark']:
        rec_spec[0] = higher_cpu
    if higher_gpu is not None:
      if rec_benchmark[1]['benchmark'] < control_gpu['benchmark']:
          rec_spec[1] = higher_gpu  
    if rec_benchmark[2] < control_memory['price']:
        rec_spec[2] = higher_memory    

    # if rec_benchmark[0]['benchmark'] < control_group['benchmark']:    
    #   rec_spec[0] = higher_cpu
    #   rec_spec[1] = higher_gpu
    #   rec_spec[2] = higher_memory
    
    # if rec_price < budget:
    #   rec_spec[0] = higher_cpu
    #   rec_spec[1] = higher_gpu  
    #   rec_spec[2] = higher_memory      
    # else:
    #   rec_spec = least_spec
    
    if use_list[0].name == "Internet" and len(use_list) == 1 and rec_price > budget:
      rec_spec = least_spec
    #=================추천 결과를 리스트로 합쳐서 serialize=====================
    result = least_spec + rec_spec
    result = filter(None, result)
    cache.set(redis_key, result)
    serializer = componentSerializer.ComponentSerializer(result, many=True)
    print(time.time() - start)
    return Response(serializer.data)


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

    if gpu is None or gpu.gpu.required_power is None:
      gpower = 300
    else:
      gpower = gpu.gpu.required_power

    if gpu is None or gpu.gpu.width is None:
      gwidth = 0
    else:
      gwidth = gpu.gpu.width

    power = component.Component.objects.select_related('power')\
      .filter(data_type=7, power__output__gte=(gpower+100))\
      .exclude(price__isnull=True).order_by('price').first()

    m_formfactor = mainboard.mainboard.formfactor.split(' ')[0]
    p_type = power.power.type.split(' ')[0]

    case = component.Component.objects.select_related('case')\
      .filter(data_type=9, case__depth__gte=(gwidth+50))\
      .exclude(price__isnull=True).order_by('price').first()
    
    result = [mainboard, hdd, ssd, power, case]
    return result

  # 더 높은 벤치마크 점수의 부품 이름과 점수를 반환
  # 객체가 없거나 호환성이 맞지 않을 때, 벤치마크 점수가 더 높은 부품을 찾기 위해 사용
  def getHigherBenchmark(self, data_type, score):
    higherBench = BenchMark.objects.filter(data_type=data_type, score__gt=score)\
      .order_by('score').first()
    return higherBench

  # 더 높은 가격의 부품을 1개 반환
  # 가격 상한선까지 견적을 높이기 위해 사용
  def getExpensiveComponent(self, data_type, price):
    expensive = component.Component.objects\
      .filter(data_type=data_type, price__gt=price)\
      .exclude(price__isnull=True)\
      .order_by('price').first()
    return expensive

  # 호환성 체크1
  # cpu, gpu, mainboard 간의 소켓 및 지원 규격 체크
  # 필드가 null이여도 호환 불가를 반환
  def checkCompatibility(self, cpu, memory, mainboard):
    result = True

    if cpu.socket is None or mainboard.socket is None:
      result = False
    elif cpu.socket != mainboard.socket:
      result = False
    if memory.type is None or cpu.memory is None:
      result = False  
    elif memory.type in cpu.memory.type:
      result = False
    if mainboard.memory_type is None or memory.type is None:  
      result = False
    elif mainboard.memory_type != memory.type:
      result = False

    return result

  # 호환성 체크2
  # mainboard, gpu, case, power 간의 폼팩터(크기) 체크
  def checkFormfactor(self, mainboard, gpu, case, power):
    result = True
    m_formfactor = mainboard.formfactor.split(' ')[0]
    g_width = gpu.width
    c_depth = case.depth
    c_type = re.findall('\(.+\)', '', case.type)
    power_type = power.type.split(' ')[0]
    power_type = re.sub('\(\w+\)', '',power_type)

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
      if llp[compare] <= rlp[compare]:
        standard_use.least_processor = uses[i].least_processor
        llp = rlp
      compare = "benchmark"
      if (llg[compare] == 0 or rlg[compare] == 0):
        compare = "price"
      if llg[compare] <= rlg[compare]:
        standard_use.least_graphics = uses[i].least_graphics
        llg = rlg
      compare = "benchmark"
      if (llm <= rlm):
        llm = rlm
      
        # 권장 사양
      if (lrp[compare] == 0 or rrp[compare] == 0):
        compare = "price"
      if lrp[compare] < rrp[compare] or standard_use.rec_processor is None:
        standard_use.rec_processor = uses[i].rec_processor
        lrp = rrp
      compare = "benchmark"
      if (lrg[compare] == 0 or rrg[compare] == 0):
        compare = "price"
      if lrg[compare] < rrg[compare] or standard_use.rec_graphics is None:
        standard_use.rec_graphics = uses[i].rec_graphics
        lrg = rrg
      if (lrm <= rrm):
        lrm = rrm
    # 용도 테이블의 요구사항 이름을 가지고 있으면 이 함수 이후에 바로 부품을 바꿀수 없기 때문에
    # 특정 Component로 교체해서 반환한다
    standard_use.least_processor = self.getCpuWithUse(standard_use.least_processor, llp['benchmark'])
    standard_use.least_graphics = self.getGpuWithUse(standard_use.least_graphics, llg['benchmark'])
    standard_use.least_memory = self.getMemoryWithUse(llm)

    if standard_use.rec_processor is not None:
      standard_use.rec_processor = self.getCpuWithUse(standard_use.rec_processor, lrp['benchmark'])
      standard_use.rec_graphics = self.getGpuWithUse(standard_use.rec_graphics, lrg['benchmark'])
      standard_use.rec_memory = self.getMemoryWithUse(lrm)
    result = [standard_use, llp, llg, llm, lrp, lrg, lrm]
    return result

  # 입력인자 : 부품명
  # 출력인자 : 입력인자에 대한 가격
  # 부품명을 포함하는 NAME을 가진 부품, price null 제외, 오름차순으로 정렬 후 1번째 반환
  def getComponentPrice(self, component_name):
    price = component.Component.objects.filter(name__icontains=component_name) \
      .only("price").exclude(price__isnull=True).order_by('price').first()
    if price is None:
      return 0
    return price.price

  #====================CPU BenchMark 점수 가져오기 ↓==================================
  cpu_mapping_before = ['코어','제온','펜티엄','셀러론','애슬론','페넘','스레드리퍼','쿼드','라이젠']
  cpu_mapping_after = ['Core ','Xeon ','Pentium ','Celeron ','Athlon ','Phenom ','TR ',' Quad ', 'Ryzen ']
  
  # 입력인자 : DB의 Component 또는 Uses Cpu name(processor)
  # 출력인자 : benchmark 점수 & 최저가 price 의 dictionary
  # cpu 1개에 대한 과정!
  def getCpuScores(self, row_name):
    zero_dictionary = {'benchmark':0, 'price':0}
    if row_name is None:
      return zero_dictionary
    mapped_name = self.cpuNameMapping(row_name)
    parsed_name = self.cpuParse(mapped_name)
    benchmark = self.getCpuBenchmark(parsed_name)
    price = self.getComponentPrice(row_name)
    result = {'benchmark':benchmark, 'price':price}
    return result
  
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
  def getCpuWithUse(self, use_name, score):
    cpu_split = self.useCpuParse(use_name)
    if len(cpu_split) > 1:
      result = component.Component.objects.select_related('cpu')\
        .filter(data_type=1)\
        .filter(name__icontains=cpu_split[0])\
        .filter(name__icontains=cpu_split[1])\
        .order_by('price').first()
    else:
      result = component.Component.objects.select_related('cpu')\
        .filter(data_type=1)\
        .filter(name__icontains=cpu_split[0])\
        .order_by('price').first()

    while(True):
      if result is not None:
        break;
      higherBenchmark = self.getHigherBenchmark(1, score)
      benchmark_name = higherBenchmark.name
      score = higherBenchmark.score
      result = self.getCpuWithBenchmark(benchmark_name)
      
    return result

  def getCpuWithBenchmark(self, benchmark_name):
    benchmark_name = benchmark_name.replace("-", " ")
    benchmark_name = benchmark_name.replace("s "," super ", 1)
    benchmark_name = re.sub('\(\w+\)', '', benchmark_name)    # 괄호 내용 삭제
    name_token = benchmark_name.split(' ')
    del name_token[0]
    if len(name_token) > 1:
      result = component.Component.objects.select_related('cpu')\
        .filter(data_type=1)\
        .filter(name__icontains=name_token[0])\
        .filter(name__icontains=name_token[1])\
        .exclude(price__isnull=True, cpu__socket__isnull=True)\
        .order_by('price').first()
    else:  
      result = component.Component.objects.select_related('cpu')\
        .filter(data_type=1)\
        .filter(name__icontains=name_token[0])\
        .exclude(price__isnull=True, cpu__socket__isnull=True)\
        .order_by('price').first()
    
    return result


  # 입력인자 : DB의 Component 또는 Uses CPU name(processor)
  # 인텔,라이젠,제온 등등 한글을 영어명칭으로 매핑하는 메소드
  # 출력인자 : 매핑이 완료된 cpu name
  def cpuNameMapping(self, row_name):
    for i in range(len(self.cpu_mapping_before)):
      row_name = row_name.replace(self.cpu_mapping_before[i], self.cpu_mapping_after[i])
    row_name.replace('  ',' ')  # 띄워쓰기 중복 없애기
    return row_name
  
  # 입력인자 : mapping이 끝난 cpu name
  # 출력인자 : 회사명, 괄호가 제거되고 split된 cpu_name 토큰 리스트
  def cpuParse(self, row_name):
    row_name = re.sub('\(\w+\)','', row_name)   # 괄호 내용은 필요없으므로 삭제
    row_name = row_name.replace("-", " ")
    row_name = re.sub("[0-9]+세대", "", row_name)  # '-[0-9]+세대' 정보 삭제
    row_name = row_name.replace(' or ', ' ')
    row_name = row_name.strip()     # 양 끝단 공백 split하기 전에 제거
    cpu_split = row_name.split(' ')
    del cpu_split[0]    # 인텔 / AMD 삭제
    return cpu_split

  # 입력인자 : 회사명, 괄호가 제거되고 split된 cpu_name 토큰 리스트
  # 출력인자 : 특정지어진다면 해당 밴치마크 점수를, 없다면 0을 반환
  def getCpuBenchmark(self, parsed_name):
    # DB에서 시리즈명으로 검색
    benchmark_list = BenchMark.objects.filter(name__icontains=parsed_name[0])   
    # 해당 시리즈에 대한 벤치마크를 전부 가져왔으므로 
    # cpu name 토큰들로 일치하는 정보를 검색
    for i in benchmark_list:
      for j in range(1, len(parsed_name)):
        index = i.name.find(parsed_name[j])
        if index != -1:
          return i.score
    if None in benchmark_list or len(benchmark_list) == 0:
      return 0
    else:
      return benchmark_list[0].score

  #====================GPU BenchMark 점수 가져오기 ↓==================================
  # Component에서는 name - manufacture & [0] 버리기, 
  # 용도 테이블에서는 특정 제품명이나 capacity을 기입 -> capacity로는 검색 불가
  # capacity로 기입되어 있을 경우, component에서 name으로 검색 -> 그 중에서

  def getGpuScores(self, row_name):
    zero_dictionary = {'benchmark':0, 'price':0}
    if row_name is None:
      return zero_dictionary
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
    if len(result) > 1:
      parsed_name = result[0] + " " + result[1]
    else:
      parsed_name = result[0]
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
  # 검색 결과가 없을 경우 벤치마크 점수가 더 높은 제품을 탐색
  # 입력인자 : 용도 테이블의 그래픽 이름
  # 출력인자 : 해당되는 종류의 그래픽 카드 중 최저가 객체 1개
  def getGpuWithUse(self, use_name, score):
    if use_name is None:      # 인터넷 서핑 용도의 경우 글카가 필요없음
      return None
    split_name = use_name.split(' ')
    del split_name[0]
    if len(split_name) > 2:
      result = component.Component.objects.select_related('gpu')\
        .filter(data_type=2)\
        .filter(name__icontains=split_name[0])\
        .filter(name__icontains=split_name[1])\
        .filter(name__icontains=split_name[2])\
        .exclude(price__isnull=True, gpu__width__isnull=True)\
        .order_by('price').first()
    else:
      result = component.Component.objects.select_related('gpu')\
        .filter(data_type=2)\
        .filter(name__icontains=split_name[0])\
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
    bracket_result = ""
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
