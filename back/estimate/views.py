from rest_framework.views   import APIView
from rest_framework.response import Response
# from .serializer import *
from .models import *
#문자열 파싱용
import re 

# Create your views here.

# 용도와 예산을 추출
# 용도 모든 사양들을 비교하여 최고치의 최소사양과 권장사양을 얻음(이게 기준/시작점이 될 것)
# 
class Recommendation(APIView):
  mapping_before = ['코어','제온','펜티엄','셀러론','애슬론','페넘','스레드리퍼']
  mapping_after = ['Core ','Xeon ','Pentium ','Celeron ','Athlon ','Phenom ','TR ']

  def get(self, request, format=None):
    uses = request.GET.getlist['uses']
    budget = request.GET.getlist['budget']
    max_spec = self.getMaxUse(uses)

  # 기본적으로 벤치마크 점수 기반으로 비교
  # 한쪽이라도 벤치마크 점수가 없을 경우
  # cpu는 clock으로, graphics와 memory는 capacity로 비교
  def getMaxUse(self, uses):
    use = uses[0]
    for i in range(1, len(uses)):
      use = self.compareUses(use, i)
    return use
  
  # 왼쪽 용도의 사양을 기준으로 오른쪽 사양을 비교하고 높으면 왼쪽에 대입
  def compareUses(self, left, right):
    try:
      if(left.rec_processor < right.rec_processor):
        left.rec_processor = right.rec_processor
      if(left.rec_graphics < right.rec_graphics):
        left.rec_graphics = right.rec_graphics
      if(left.rec_memory < right.rec_memory):
        left.rec_memory = right.rec_memory
      if(left.least_processor < right.least_processor):
        left.least_processor = right.least_processor
      if(left.least_graphics < right.least_graphics):
        left.least_graphics = right.least_graphics
      if(left.least_memory < right.least_memory):
        left.least_memory = right.least_memory
    except:
      pass
    return left



  #====================CPU BenchMark 점수 가져오기 ↓==================================
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
    row_name.strip()     # 양 끝단 공백 split하기 전에 제거
    row_name.replace(' or ', ' ')
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
    # 입력인자 : DB의 Component 또는 Uses GPU name(graphics)
    # 출력인자 : 매핑이 완료된 gpu name    
    # def gpuParse(self, row_name):
    #   for i in range(len(self))