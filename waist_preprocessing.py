from pymongo import MongoClient
import json
import plotly

my_client = MongoClient("mongodb://localhost:27017/")
db = my_client.healthcheck
healthCheckup = db.health
obesity=db.obesity

#허리둘레에 따라 비만도와 영향이 있는지에 대한 고찰-주현
# BMI 지수는 몸무게/키^2
# 저체중 18.5 정상체중 23 과체중 25 경도비만 30 중정도비만 35 고도비만

def calc_bmi():
    output_file_name="./data/calc_bmi.json"
    with open(output_file_name, "w", encoding="UTF-8", newline="") as output_file:      #쓰기모드로 열어서 json.dump로 직렬화
        bmi_list = {}
        bmi_list['BMI'] = []
        # hap=0.0
        # avg_man=0.0
        # avg_woman=0.0
        # hap2=0.0
        # count=0
        # count2=0

        # for data2 in healthCheckup.find():
        #     if data2['성별코드'] == "1":  #남자일때
        #         if(str(data2['허리둘레'])!=''):
        #             hap+=float(str(data2['허리둘레']))
        #         else:
        #             count=count+1
        #     else:
        #         if (str(data2['허리둘레']) != ''):
        #             hap2 +=float(str(data2['허리둘레']))
        #         else:
        #             count2=count2+1
        #
        # avg_man=hap/(len(data2)-count)
        # avg_woman=hap2/(len(data2)-count2)


        for data in healthCheckup.find():
            if data['성별코드'] == "1":
                if data['허리둘레']!='':
                    bmi_list['BMI'].append({"성별": '남',
                                        "신장(cm)": int(data['신장(5Cm단위)']),
                                        "체중(kg)": int(data['체중(5Kg 단위)']),
                                        "허리둘레": float(data['허리둘레']),
                                        "BMI": round(10000 * int(data['체중(5Kg 단위)']) /
                                               (int(data['신장(5Cm단위)']) * int(data['신장(5Cm단위)'])),1),
                                        })
            else:
                if data['허리둘레']!='':
                     bmi_list['BMI'].append({"성별": '여',
                                        "신장(cm)": int(data['신장(5Cm단위)']),
                                        "체중(kg)": int(data['체중(5Kg 단위)']),
                                        "허리둘레": float(data['허리둘레']),
                                        "BMI": round(10000 * int(data['체중(5Kg 단위)']) /
                                               (int(data['신장(5Cm단위)']) * int(data['신장(5Cm단위)'])),1),
                                        })
        json.dump(bmi_list, output_file, indent=4, ensure_ascii=False)
        obesity.insert_many(bmi_list['BMI'])


calc_bmi()

#여성일때 허리둘레, 남성일때 허리둘레