from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.healthCheckup
obesity_total = db.obesity_total

# idx_before
print("idx_before")
print(db.obesity_total.find({"가입자 일련번호": 767784}).explain()['executionStats'])
# index
db.obesity_total.create_index('BMI')
# idx_after
print("idx_after")
print(db.obesity_total.find({"가입자 일련번호": 767784}).explain()['executionStats'])