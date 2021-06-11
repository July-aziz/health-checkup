from pymongo import MongoClient
import json
import plotly

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.health
obesity_waist = db.obesity_waist


#허리둘레에 따라 비만도와 영향이 있는지에 대한 고찰-주현
# BMI 지수는 몸무게/키^2
# 저체중 18.5 정상체중 23 과체중 25 경도비만 30 중정도비만 35 고도비만

def calc_bmi_3():
    output_file_name="./data/calc_bmi_3.json"
    with open(output_file_name, "w", encoding="UTF-8", newline="") as output_file: # 쓰기모드로 열어서 json.dump로 직렬화
        bmi_list = {}
        bmi_list['BMI'] = []

        for data in healthCheckup.find():
            if data['성별코드'] == "1":
                if str(data['허리둘레']) != '':
                    if float(data['허리둘레']) >= 30:  # 허리둘레 값이 없는 row과 30이하인 비정상 값을 가진 row는 제외
                        bmi_list['BMI'].append({"성별": '남',
                                                "신장(cm)": int(data['신장(5Cm단위)']),
                                                "체중(kg)": int(data['체중(5Kg 단위)']),
                                                "허리둘레": float(data['허리둘레']),
                                                "BMI": round(10000 * int(data['체중(5Kg 단위)']) /
                                                             (int(data['신장(5Cm단위)']) * int(data['신장(5Cm단위)'])), 1),
                                                })
            else:
                if str(data['허리둘레']) != '':
                    if float(data['허리둘레']) >= 30:
                        bmi_list['BMI'].append({"성별": '여',
                                                "신장(cm)": int(data['신장(5Cm단위)']),
                                                "체중(kg)": int(data['체중(5Kg 단위)']),
                                                "허리둘레": float(data['허리둘레']),
                                                "BMI": round(10000 * int(data['체중(5Kg 단위)']) /
                                                             (int(data['신장(5Cm단위)']) * int(data['신장(5Cm단위)'])), 1),

                                                })
        json.dump(bmi_list, output_file, indent=4, ensure_ascii=False)
        obesity_waist.insert_many(bmi_list['BMI'])


calc_bmi_3()

#여성일때 허리둘레, 남성일때 허리둘레
