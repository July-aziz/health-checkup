# 데이터 분석

## 🏥 건강검진 데이터 상관분석 🏥
1. 건강검진 데이터의 상관관계분석 그래프

실행 명령어 : `` python3 heatmap.py ``

![heatmap](https://user-images.githubusercontent.com/48914904/121794467-42c4c900-cc43-11eb-82ef-941d3d0c8758.png)

## 🍺 음주여부와 비만도 🍺
1. 데이터 전처리 단계

비만도(BMI)를 계산하고 음주데이터를 추출해서 새로운 collection에 저장한다.

실행 명령어 : `` python3 preprocessing_drinking.py ``

<br>

2. 음주여부별 BMI평균 비교 그래프

실행 명령어 : `` python3 obesity-drinking_1.py ``

![drink1](https://user-images.githubusercontent.com/48914904/121794470-5c661080-cc43-11eb-96eb-da9316408c81.png)

➔ 음주를 하는 사람의 BMI평균이 더 높다.

<br>

3. 음주여부별 BMI 분포 비율 비교 그래프

실행 명령어 : `` python3 obesity-drinking_2.py ``

![drink2](https://user-images.githubusercontent.com/48914904/121794478-6e47b380-cc43-11eb-9fe5-849200a7e3f6.png)

➔ 음주를 하지 않은 사람이 정상체중의 비율이 높고, 음주를 하는 사람은 과체중의 비율이 높다.

<br>

---

# 최적화
## 인덱싱(indexing)

- 테이블에 대한 검색의 속도를 높여주는 자료 구조
- 메모리 영역에 일종의 목차를 생성하는 개념
- 이런 목차를 이용하여 검색 범위를 줄여 속도를 높일 수 있다.

실행 명령어 : `` python3 index.py ``

➔ 속도 비교

## 샤딩(sharding)

- 하나의 거대한 데이터베이스나 네트워크 시스템을 여러 개의 작은 조각으로 나누어 분산 저장하여 관리하는 것
- 단일의 데이터를 다수의 데이터베이스로 쪼개어 나누는 걸 말하는데, 단일의 데이터베이스에서 저장하기 너무 클 때 사용하여 데이터를 구간별로 쪼개어 나눔으로써 노드에 무겁게 가지고 있던 데이터를 빠르게 검증할 수 있어 빠른 트랜잭션 속도를 향상시킬 수 있다. 

➔ 속도 비교
