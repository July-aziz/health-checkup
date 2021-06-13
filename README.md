## 건강검진데이터에서 비만도와 상관관계가 있는 요소
- 혈압이 높은 사람이 비만도가 더 높은지에 대한 고찰
- 허리둘레에 따라 비만도와 영향이 있는지에 대한 고찰
- 음주여부에 따라 비만도와 영향이 있는지에 대한 고찰

### 🏥 건강검진 데이터 상관분석 🏥
1. 건강검진 데이터의 상관관계분석 그래프

실행 명령어 : `` python3 heatmap.py ``

![heatmap](https://user-images.githubusercontent.com/48914904/121794467-42c4c900-cc43-11eb-82ef-941d3d0c8758.png)

### 🍺 음주여부와 비만도 🍺
1. 데이터 전처리 단계

비만도(BMI)를 계산하고 음주데이터를 추출해서 새로운 collection에 저장한다.

실행 명령어 : `` python3 preprocessing_drinking.py ``

2. 음주여부별 BMI평균 비교 그래프

실행 명령어 : `` python3 obesity-drinking_1.py ``

![drink1](https://user-images.githubusercontent.com/48914904/121794470-5c661080-cc43-11eb-96eb-da9316408c81.png)

➔ 음주를 하는 사람의 BMI평균이 더 높다.

3. 음주여부별 BMI 분포 비율 비교 그래프

실행 명령어 : `` python3 obesity-drinking_2.py ``

![drink2](https://user-images.githubusercontent.com/48914904/121794478-6e47b380-cc43-11eb-9fe5-849200a7e3f6.png)

➔ 음주를 하지 않은 사람이 정상체중의 비율이 높고, 음주를 하는 사람은 과체중의 비율이 높다.