import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.health
obesity_bloodpressure = db.obesity_bloodpressure


# BMI 지수는 몸무게/키^2
# 저체중 18.5 정상체중 23 과체중 25 경도비만 30 중정도비만 35 고도비만
def calc_bmi_2():
    output_file_name = "./data/calc_bmi_2.json"
    with open(output_file_name, "w", encoding="UTF-8", newline="") as output_file:
        bmi_list = {}
        bmi_list['BMI'] = []

        for data in healthCheckup.find():
            if data['수축기 혈압'] != "" and data['이완기 혈압'] != "": # null값 제외
                bmi_list['BMI'].append({"가입자 일련번호": data['가입자 일련번호'],
                                        "신장(cm)": int(data['신장(5Cm단위)']),
                                        "체중(kg)": int(data['체중(5Kg 단위)']),
                                        "BMI": 10000 * int(data['체중(5Kg 단위)']) /
                                               (int(data['신장(5Cm단위)']) * int(data['신장(5Cm단위)'])),
                                        "수축기 혈압": int(data['수축기 혈압']),
                                        "이완기 혈압": int(data['이완기 혈압']),
                                        })

        json.dump(bmi_list, output_file, indent=4, ensure_ascii=False)
        obesity_bloodpressure.insert_many(bmi_list['BMI'])


calc_bmi_2()
