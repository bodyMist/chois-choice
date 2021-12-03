from rest_framework.views   import APIView
from rest_framework.response import Response
# from .serializer import *
from .models import *
from ..component import models as component

#문자열 파싱용
import re 

# Create your views here.

# 용도와 예산을 추출
# 용도 모든 사양들을 비교하여 최고치의 최소사양과 권장사양을 얻음(이게 기준/시작점이 될 것)
# 시작점에서는 cpu, gpu, memory만 있으므로 용도별?로 Hdd/Ssd, mainboard, cooler, case를 선택
# 예)인터넷 서핑용 - Hdd250GB, Ssd 128gb 이상, mainboard는 cpu 소켓에 맞춰서 
# 
class Recommendation(APIView):
  
  def get(self, request, format=None):
    uses_name = request.GET.getlist['uses']     # 용도는 다수 입력이 가능(이름만 넘어옴)
    budget = request.GET.get['budget']
    current_price = 0                           # 현재 견적에서의 총 가격
    use_list = []
    for use in uses_name:
      target = Uses.objects.filter(name = use)  # 용도 이름으로 각각 용도 객체 검색
      use_list.append(target)                   # 용도 리스트에 추가
    max_spec = self.getMaxUse(use_list)         # 용도 리스트에 대해 최고치 사양 구하기
    


  # 입력인자 : 부품명
  # 출력인자 : 입력인자에 대한 가격
  # 부품명을 포함하는 NAME을 가진 부품, price null 제외, 오름차순으로 정렬 후 1번째 반환
  def getComponentPrice(self, component_name):
    try:
      price = component.Component.objects.filter(name__icontains=component_name) \
      .only("price").exclude(price__isnull=True).order_by('price')
    except:
      price = 0   # 가격 정보가 없을 경우 0을 기입
    return price


  # 입력인자 : 비교할 용도 리스트
  # 출릭인자 : 비교,계산,대입이 끝난 용도 객체 하나, 
  #           해당 객체에 대한 각 {벤치마크 점수와 가격 정보}로 이루어진 리스트
  #           ex) [Uses 객체, 최소cpu 점수 dict, 최소gpu 점수 dict, ...]
  # 기본적으로 벤치마크 점수 기반으로 비교
  # 한쪽이라도 벤치마크 점수가 없을 경우 가격 정보로 비교
  def getMaxUse(self, uses):
    standard_use = uses[0]
    zero_dictionary = {'benchmark':0, 'price':0}
    # 1번 용도에 대해 benchmark와 가격 얻기
    # 최소사양
    llp = self.getCpuScores(standard_use.least_processor)
    llg = standard_use.least_graphic
    llm = standard_use.least_memory
    # 권장사양
    # 있다면 점수를 계산하지만, 없다면 0점 dictionary 할당
    lrp = self.getCpuScores(standard_use.rec_processor) \
       if standard_use.rec_processor is not None else zero_dictionary
    lrg = standard_use.rec_graphic if standard_use.rec_graphic is not None else zero_dictionary
    lrm = standard_use.rec_memory if standard_use.rec_memory is not None else zero_dictionary

    for i in range(1, len(uses)):
      # 비교대상이 될 용도들에 대해서 benchmark와 가격 계산
      rlp = self.getCpuScores(uses[i].least_processor)
      rlg = uses[i].least_graphic
      rlm = uses[i].least_memory
      rrp = self.getCpuScores(uses[i].rec_processor) \
       if standard_use.rec_processor is not None else zero_dictionary
      rrg = uses[i].rec_graphic if uses[i].rec_graphic is not None else zero_dictionary
      rrm = uses[i].rec_memory if uses[i].rec_memory is not None else zero_dictionary

      # 계산 후 대조군과 비교 대입하기
      # 최소 사양
      if llp['benchmark'] < rlp['benchmark']:
        standard_use.least_processor = uses[i].least_processor
      if llg['benchmark'] < rlg['benchmark']:
        standard_use.least_graphic = uses[i].least_graphic
      if llm['benchmark'] < rlm['benchmark']:
        standard_use.least_memory = uses[i].least_memory
      # 권장 사양
      if lrp['benchmark'] < rrp['benchmark']:
        standard_use.rec_processor = uses[i].rec_processor
      if lrg['benchmark'] < rrg['benchmark']:
        standard_use.rec_graphic = uses[i].rec_graphic
      if lrm['benchmark'] < rrm['benchmark']:
        standard_use.rec_memory = uses[i].rec_memory
    result = [standard_use, llp, llg, llm, lrp, lrg, lrm]
    return result


  # 용도 || 부품 의 벤치마크, 가격 정보 비교
  def compareScore(self, left, right):
    if (left['benchmark'] == 0 or right['benchmark'] == 0):
      left = right if left['price'] < right['price'] else left
    else:
      left = right if left['benchmark'] < right['benchmark'] else left
    return left


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

  # 입력인자 : split된 uses cpu name의 토큰 리스트
  # 토큰 리스트를 이용해서 가격이 가장 낮은 cpu component 반환
  # 출력인자 : 해당되는 cpu component
  def getCpuWithUse(self, cpu_split):
    result = component.Component.objects.filter(data_type=1, 
    name__icontains=cpu_split[0], name__icontains=cpu_split[1]).order_by('price')
    return result



  # 입력인자 : DB의 Component 또는 Uses CPU name(processor)
  # 인텔,라이젠,제온 등등 한글을 영어명칭으로 매핑하는 메소드
  # 출력인자 : 매핑이 완료된 cpu name
  def cpuNameMapping(self, row_name):
    for i in range(len(self.mapping_before)):
      row_name.replace(self.mapping_before[i], self.mapping_after[i])
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

  def getComparableScores(self, row_name):
    mapped_name = self.gpuMapping(row_name)
    parsed_name = self.gpuParse(mapped_name)
    benchmark = self.getGpuBenchmark(parsed_name)
    price = self.getComponentPrice(row_name)

  # super->s , ti -> -ti, xt -> -XT
  # 입력인자 : DB의 Component(data_type=2) 또는 Uses GPU name(graphics)
  # 출력인자 : 맨 앞 제조사명과 종류(지포스, 라데온)가 삭제되고 일부 명칭이 다시 매핑된 name
  def gpuMapping(self, row_name, manufactor):
    row_name = row_name.lower()
    row_name.replace(manufactor, "" , 1)
    row_name.replace("확인중", "")
    row_name.replace(" ti", "-Ti" , 1)
    row_name.replace(" super ", "s ", 1)
    row_name.replace(" xt ", "-XT ", 1)
    if row_name.startswith('gtx'):
      row_name = row_name.replace("gtx", "gtx ") 
    elif row_name.startswith('gt'):
      row_name = row_name.replace("gt", "gt ")
    row_name.strip()
    return row_name
  
  # 입력인자 : 매핑이 완료된 gpu name
  # 출력인자 : 매칭 검색을 하기 위한 parsed_name
  # 예상출력 : GTX 1060-Ti, 
  def gpuParse(self, mapped_name):
    mapped_name = re.sub('[0-9]+GB',"", mapped_name)  # 용도나 gpu_name의 capacity 삭제
    result = mapped_name.split(' ')
    parsed_name = result[0] + " " + result[1]
    return parsed_name

  # 입력인자 : 매칭 검색이 가능한 parsed name / 시리즈명+제품명 구성 (gtx 1060)
  def getGpuBenchmark(self, parsed_name):
    # icontains를 사용하면 ti버전이나 super 버전, (Mobile)이 딸려올 수 있음
    # 점수 기준으로 내림차순 정렬로 가져오기
    benchmark_list = BenchMark.objects.filter(name__icontains=parsed_name)\
    .order_by('-score')
    
    # 정확하게 일치하는 name이 있을 경우, 해당 벤치 점수를 채택
    # 1060는 3GB 5GB 버전으로 나뉘어서 이에 대한 예외처리로 정규식 파싱교체 사용
    for i in benchmark_list:
      i = re.sub('-[0-9]GB', '', i)
      if parsed_name == i.name:
        return i.score
    return 0


  #====================MEMORY BenchMark 점수 가져오기 ↓=============================
  # Memory는 시리즈명(Trident, Fury, Vengeance 등) + 클럭(3200) + 용량(2x8G) 정보로 검색 가능
  # Memory BenchMark 데이터가 굉장히 적음(약 100개)
  # 
  memory_series = ['Vengeance', 'Trident', 'Ripjaws', 'Dominator', 'Ballistix', 'Predator']

  # 입력인자 : DB Component memory name
  # 출력인자 : 
  def gpuParse(self, row_name):
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
    benchmark_list= BenchMark.objects.filter(name__icontains=parsed_name[0],
    name__icontains=parsed_name[1], name__icontains=parsed_name[2], 
    name__icontains=parsed_name[3]).order_by('-score')

    if len(benchmark_list) == 0:
      return 0
    return benchmark_list[0]
