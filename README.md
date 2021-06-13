# 데이터 분석

## 데이터셋 설명
- 파일데이터명 : 국민건강보험공단_건강검진정보_20191231
- 제공기관 : 국민건강보험공단
- 기준년도 : 2019년  
- 설명 : 건강검진정보란 국민건강보험의 직장가입자와 40세 이상의 피부양자, 세대주인 지역가입자와 40세 이상의 지역가입자의 
  일반건강검진 결과와 이들 일반건강검진 대상자 중에 만40세와 만66세에 도달한 이들이 받게 되는 생애전환기건강진단 
  수검이력이 있는 각 연도별 수진자 <u>**100만 명**</u>에 대한 기본정보(성, 연령대, 시도코드 등)와 검진내역(신장, 체중, 총콜레스테롤, 혈색소 등)으로 
  구성된 개방데이터입니다.
- 출처 : [공공데이터포털](https://www.data.go.kr/data/15007122/fileData.do)

## 🏥 건강검진 데이터 상관분석 🏥
**1. 건강검진 데이터의 상관관계분석 그래프**

실행 명령어 : `` python3 heatmap.py ``

![heatmap](https://user-images.githubusercontent.com/48914904/121794467-42c4c900-cc43-11eb-82ef-941d3d0c8758.png)

## 🍺 음주여부와 비만도 🍺
**1. 데이터 전처리 단계**

비만도(BMI)를 계산하고 음주데이터를 추출해서 새로운 collection에 저장한다.

실행 명령어 : `` python3 preprocessing_drinking.py ``

<br>

**2. 음주여부별 BMI평균 비교 그래프**

실행 명령어 : `` python3 obesity-drinking_1.py ``

![drink1](https://user-images.githubusercontent.com/48914904/121794470-5c661080-cc43-11eb-96eb-da9316408c81.png)

➔ 음주를 하는 사람의 BMI평균이 더 높다.

<br>

**3. 음주여부별 BMI 분포 비율 비교 그래프**

실행 명령어 : `` python3 obesity-drinking_2.py ``

![drink2](https://user-images.githubusercontent.com/48914904/121794478-6e47b380-cc43-11eb-9fe5-849200a7e3f6.png)

➔ 음주를 하지 않은 사람이 정상체중의 비율이 높고, 음주를 하는 사람은 과체중의 비율이 높다.

<br>

---

## 💓 혈압과 비만도 💓
**1. 데이터 전처리 단계**

비만도(BMI)를 계산하고 혈압(수축기 혈압/이완기 혈압)을 추출해서 새로운 collection에 저장한다.

실행 명령어 : `` python3 preprocessing_bloodpressure.py ``

<br>

cf) 데이터 확인 쿼리

실행 명령어 : `` python3 obesity_bloodpressure1.py ``

<br>

**2. 수축기 혈압과 BMI 평균 비교 그래프**

실행 명령어 : `` python3 obesity_bloodpressure2.py ``

![수축기&BMI](https://user-images.githubusercontent.com/48914872/121795518-97207680-cc4c-11eb-8ae9-d4604003e636.JPG)

➔ 수축기 혈압이 높을수록 BMI평균이 높아지다가 마지막에 낮아진다.

<br>

**3. 이완기 혈압과 BMI 평균 비교 그래프**

실행 명령어 : `` python3 obesity_bloodpressure3.py ``

![이완기&BMI](https://user-images.githubusercontent.com/48914872/121795564-f8484a00-cc4c-11eb-9bbf-6a02d0a7e508.JPG)

➔ 이완기 혈압이 높을수록 BMI평균이 높아지다가 마지막에 낮아진다.

<br>

**4. 수축기 혈압과 이완기 혈압 비교 그래프**

실행 명령어 : `` python3 obesity_bloodpressure4.py ``

![이완기&수축기](https://user-images.githubusercontent.com/48914872/121795576-12822800-cc4d-11eb-8f00-73777a6e09da.JPG)

➔ 이완기 혈압과 수축기 혈압이 비례하다.


⇒ 혈압이 높을수록 BMI평균이 높다가 마지막에 낮아진다.

<br>

---

## 📏 허리둘레과 비만도 📏
**1. 데이터 전처리 단계**

비만도(BMI)를 계산하고 허리둘레를 추출해서 새로운 collection에 저장한다.

실행 명령어 : `` python3 waist_preprocessing.py ``

<br>

**2. 비만도별 허리둘레 평균 비교 그래프 & BMI별 평균 허리둘레 기준보다 낮고 큼의 비율**

실행 명령어 : `` python3 waist_obesity.py ``

![newplot (4)](https://user-images.githubusercontent.com/48914904/121802904-dfa25900-cc79-11eb-9416-e247bf8ececb.png)

➔ 여자보단 남자의 허리둘레 평균이 더 크다. BMI지수가 높아질수록 허리둘레가 커진다.

<br>

![newplot (3)](https://user-images.githubusercontent.com/48914904/121802910-e5983a00-cc79-11eb-8ed6-dfcce80e5828.png)

➔ BMI지수가 높아질수록 평균 허리둘레보다 큰 사람이 많다.

<br>

---

# 최적화
## 인덱싱(indexing)

- 테이블에 대한 검색의 속도를 높여주는 자료 구조
- 메모리 영역에 일종의 목차를 생성하는 개념
- 이런 목차를 이용하여 검색 범위를 줄여 속도를 높일 수 있다.

실행 명령어 : `` python3 index.py ``

속도 비교 : 

|구분|인덱싱 전|인덱싱 후|
|:---:|:---:|:---:|
|혈압|`75.2370`|`30.7187`|
|허리둘레|`0.1249`|`0.0818`|
|음주여부|`74.7378`|`57.4922`|

➔ 인덱싱을 한 뒤 퀴리문의 실행시간이 감소했다.

## 샤딩(sharding)

- 하나의 거대한 데이터베이스나 네트워크 시스템을 여러 개의 작은 조각으로 나누어 분산 저장하여 관리하는 것
- 단일의 데이터를 다수의 데이터베이스로 쪼개어 나누는 걸 말하는데, 단일의 데이터베이스에서 저장하기 너무 클 때 사용하여 데이터를 구간별로 쪼개어 나눔으로써 노드에 무겁게 가지고 있던 데이터를 빠르게 검증할 수 있어 빠른 트랜잭션 속도를 향상시킬 수 있다. 

속도 비교 :

|구분|샤딩 전|샤딩 후|
|:---:|:---:|:---:|
|`기준쿼리`|`10.1234`|`5.4321`|

➔ 샤딩을 한 뒤 퀴리문의 실행시간이 감소했다.
