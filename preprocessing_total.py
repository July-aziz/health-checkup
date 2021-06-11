import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.health
obesity_total = db.obesity_total

# BMI 지수는 몸무게/키^2
# 저체중 18.5 정상체중 23 과체중 25 경도비만 30 중정도비만 35 고도비만
def calc_bmi_total():
    output_file_name = "./data/calc_bmi_total.json"
    with open(output_file_name, "w", encoding="UTF-8", newline="") as output_file:
        bmi_list = {}
        bmi_list['BMI'] = []

        for data in healthCheckup.find():
            if data['음주여부'] == "1":
                if data['성별코드'] == "1":
                    if data['수축기 혈압'] != "" and data['이완기 혈압'] != "":  # null값 제외
                        if str(data['허리둘레']) != '':
                            if float(data['허리둘레']) >= 30:  # 허리둘레 값이 없는 row과 30이하인 비정상 값을 가진 row는 제외
                                bmi_list['BMI'].append({"성별": '남',
                                                        "신장(cm)": int(data['신장(5Cm단위)']),
                                                        "체중(kg)": int(data['체중(5Kg 단위)']),
                                                        "음주여부": 1,
                                                        "수축기 혈압": int(data['수축기 혈압']),
                                                        "이완기 혈압": int(data['이완기 혈압']),
                                                        "허리둘레": float(data['허리둘레']),
                                                        "BMI": round(10000 * int(data['체중(5Kg 단위)']) /
                                                                     (int(data['신장(5Cm단위)']) * int(data['신장(5Cm단위)'])),
                                                                     1),
                                                        })
                else:
                    if data['수축기 혈압'] != "" and data['이완기 혈압'] != "":  # null값 제외
                        if str(data['허리둘레']) != '':
                            if float(data['허리둘레']) >= 30:
                                bmi_list['BMI'].append({"성별": '여',
                                                        "신장(cm)": int(data['신장(5Cm단위)']),
                                                        "체중(kg)": int(data['체중(5Kg 단위)']),
                                                        "음주여부": 1,
                                                        "수축기 혈압": int(data['수축기 혈압']),
                                                        "이완기 혈압": int(data['이완기 혈압']),
                                                        "허리둘레": float(data['허리둘레']),
                                                        "BMI": round(10000 * int(data['체중(5Kg 단위)']) /
                                                                     (int(data['신장(5Cm단위)']) * int(data['신장(5Cm단위)'])),
                                                                     1),

                                                        })
            else:
                if data['성별코드'] == "1":
                    if data['수축기 혈압'] != "" and data['이완기 혈압'] != "":  # null값 제외
                        if str(data['허리둘레']) != '':
                            if float(data['허리둘레']) >= 30:  # 허리둘레 값이 없는 row과 30이하인 비정상 값을 가진 row는 제외
                                bmi_list['BMI'].append({"성별": '남',
                                                        "신장(cm)": int(data['신장(5Cm단위)']),
                                                        "체중(kg)": int(data['체중(5Kg 단위)']),
                                                        "음주여부": 0,
                                                        "수축기 혈압": int(data['수축기 혈압']),
                                                        "이완기 혈압": int(data['이완기 혈압']),
                                                        "허리둘레": float(data['허리둘레']),
                                                        "BMI": round(10000 * int(data['체중(5Kg 단위)']) /
                                                                     (int(data['신장(5Cm단위)']) * int(data['신장(5Cm단위)'])),
                                                                     1),
                                                        })
                else:
                    if data['수축기 혈압'] != "" and data['이완기 혈압'] != "":  # null값 제외
                        if str(data['허리둘레']) != '':
                            if float(data['허리둘레']) >= 30:
                                bmi_list['BMI'].append({"성별": '여',
                                                        "신장(cm)": int(data['신장(5Cm단위)']),
                                                        "체중(kg)": int(data['체중(5Kg 단위)']),
                                                        "음주여부": 0,
                                                        "수축기 혈압": int(data['수축기 혈압']),
                                                        "이완기 혈압": int(data['이완기 혈압']),
                                                        "허리둘레": float(data['허리둘레']),
                                                        "BMI": round(10000 * int(data['체중(5Kg 단위)']) /
                                                                     (int(data['신장(5Cm단위)']) * int(data['신장(5Cm단위)'])),
                                                                     1),

                                                        })

        json.dump(bmi_list, output_file, indent=4, ensure_ascii=False)
        obesity_total.insert_many(bmi_list['BMI'])


calc_bmi_total()
