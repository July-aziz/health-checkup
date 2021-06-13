from pymongo import MongoClient
import time  # 인덱싱 전후 시간 비교를 위해서

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.health
obesity_bloodpressure = db.obesity_bloodpressure

start = time.time()  # 시작 시간 저장

# # 최고-최저 확인
s_q1=db.obesity_bloodpressure.aggregate([  # 수축기 혈압 최저
  {'$project':{"수축기 혈압" : 1, "_id": 0}},
  {'$sort':{"수축기 혈압" : 1}},
  {'$limit':5}
])
s_q2=db.obesity_bloodpressure.aggregate([  # 수축기 혈압 최고
  {'$project':{"수축기 혈압" : 1, "_id": 0}},
  {'$sort':{"수축기 혈압" : -1}},
  {'$limit':5}
])
r_q1=db.obesity_bloodpressure.aggregate([  # 이완기 혈압 최저
  {'$project':{"이완기 혈압" : 1, "_id": 0}},
  {'$sort':{"이완기 혈압" : 1}},
  {'$limit':5}
])
r_q2=db.obesity_bloodpressure.aggregate([  # 이완기 혈압 최고
  {'$project':{"이완기 혈압" : 1, "_id": 0}},
  {'$sort':{"이완기 혈압" : -1}},
  {'$limit':5}
])

# # 수축기 혈압 & BMI
s_q3=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':56, '$lte':75}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q4=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':76, '$lte':95}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q5=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':96, '$lte':115}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q6=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':116, '$lte':135}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q7=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':136, '$lte':155}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q8=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':156, '$lte':175}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q9=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':176, '$lte':195}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q10=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':196, '$lte':215}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q11=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':216, '$lte':235}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q12=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':236, '$lte':255}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
s_q13=db.obesity_bloodpressure.aggregate([
  {'$match':{"수축기 혈압":{'$gte':256, '$lte':275}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])

# # 이완기 혈압 & BMI
r_q3=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':26, '$lte':45}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
r_q4=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':46, '$lte':65}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
r_q5=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':66, '$lte':85}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
r_q6=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':86, '$lte':105}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
r_q7=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':106, '$lte':125}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
r_q8=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':126, '$lte':145}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
r_q9=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':146, '$lte':165}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
r_q10=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':166, '$lte':185}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])
r_q11=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':186, '$lte':205}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
])

# # 이완기 혈압 & 수축기 혈압
m_q1=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':26, '$lte':45}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$수축기 혈압'}}}
])
m_q2=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':46, '$lte':65}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$수축기 혈압'}}}
])
m_q3=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':66, '$lte':85}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$수축기 혈압'}}}
])
m_q4=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':86, '$lte':105}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$수축기 혈압'}}}
])
m_q5=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':106, '$lte':125}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$수축기 혈압'}}}
])
m_q6=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':126, '$lte':145}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$수축기 혈압'}}}
])
m_q7=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':146, '$lte':165}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$수축기 혈압'}}}
])
m_q8=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':166, '$lte':185}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$수축기 혈압'}}}
])
m_q9=db.obesity_bloodpressure.aggregate([
  {'$match':{"이완기 혈압":{'$gte':186, '$lte':205}}},
  {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$수축기 혈압'}}}
])

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
