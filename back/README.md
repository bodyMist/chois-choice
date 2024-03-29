# Chois-choice
필터링 기반 조립식 컴퓨터 추천 웹 사이트 개발 프로젝트

## 사용 기술
- Django
- DjangoRestFramework
- Mysql
- Redis
### 기술 채택 이유
 - Django : 짧은 개발 일정에 맞추기 위해 빠른 개발이 가능한 django를 선택
 - Mysql : Django의 ORM 사용 및 컴퓨터 부품 데이터의 정합성, 무결성이 중요했기 때문
 - Redis : Python의 태생적 단점에 더불어 주요 기능의 빈번한 DB 접근으로 인한 느린 속도를 개선하기 위함

## 주요 기능
* 부품-리스트 출력
* 특정 부품 상세 정보
* 부품 리스트 출력
* 특정 부품 검색
* 견적 추천
  - 사용자로부터 용도와 금액을 입력받음
  - 사전에 입력된 용도 테이블의 데이터를 기준으로 최소 사양과 권장 사양을 추출
  - 사양의 금액과 사용자의 예산을 비교하여 부품을 벤치마크 점수를 기준으로 upscaling
 
 ## ISSUE
 1. 견적 추천 기능의 속도 개선
    - 많은 DB 접근과 다수의 반복문으로 인한 기능의 반환시간이 평균 약 6초 소요
    - 사용자는 2초 이상의 실행 시간에는 '느리다'라고 판단하기 때문에 방법을 강구
    - Redis를 이용하여 key=사용자의 입력, value=견적 결과를 저장하고 동일한 요청에 대해 Redis에서 반환
    - 결과적으로 동일 요청에 대해 10ms 이하의 성능을 보장

## 동작 화면
<p align="left">
<img src="https://user-images.githubusercontent.com/77658870/202624401-39b650fb-1fac-480d-a757-305d2e464529.png" width="350" height="400"/>
<img src="https://user-images.githubusercontent.com/77658870/202624405-177a0acd-7a0f-458a-a131-048c9e114db1.png" width="300" height="400"/>
<img src="https://user-images.githubusercontent.com/77658870/202624415-d7a66854-d665-4adf-8673-4fb40cc06559.png" width="350" height="400"/>
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/77658870/202624411-11ec47c8-ea5f-4929-ad3a-13ba220f28a3.png" height="400"/>
</p>
