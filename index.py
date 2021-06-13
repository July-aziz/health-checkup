from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.healthCheckup
obesity_total = db.obesity_total

# index
db.obesity_total.create_index('BMI')  # 인덱싱


###### mongo에서 쿼리 하나당 실행속도 비교하는 코드
###### aggregate의 explain은 mongo에서만 가능
###### 인덱싱은 pymongo 가능
###### mongo 코드 작성해놓음

# # idx_before
# # 혈압 쿼리
# query_b=db.obesity_total.explain("executionStats").aggregate([
#   {'$match':{"수축기 혈압":{'$gte':156, '$lte':175}}},
#   {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
# ])

# # 음주여부 쿼리
# query_d = db.obesity_total.explain("executionStats").aggregate([
#     {'$match': {
#         'BMI': {'$lt': 18.5}
#     }
#     },
#     {'$group': {
#         '_id': '$음주여부',
#         'count': {'$sum': 1}
#     }
#     }
# ])

# # 허리둘레 쿼리
# query_w = db.obesity_total.explain("executionStats").aggregate([
#     {'$match':{
#         'BMI':{'$lt':18.5}
#         }
#     },
#     {'$group':{
#         '_id':'$성별','avg_waist':{'$avg':'$허리둘레'}
#         }
#     }
# ])

# # index
# db.obesity_total.create_index('BMI')  # 인덱싱은 pymongo 가능
# ## db.obesity_total.ensureIndex({"BMI":1})  # mongo 실행 코드

# # idx_after
# # 혈압 쿼리
# query_b=db.obesity_total.explain("executionStats").aggregate([
#   {'$match':{"수축기 혈압":{'$gte':156, '$lte':175}}},
#   {'$group':{'_id':'null', 'avg_BMI':{'$avg':'$BMI'}}}
# ])

# # 음주여부 쿼리
# query_d = db.obesity_total.explain("executionStats").aggregate([
#     {'$match': {
#         'BMI': {'$lt': 18.5}
#     }
#     },
#     {'$group': {
#         '_id': '$음주여부',
#         'count': {'$sum': 1}
#     }
#     }
# ])

# # 허리둘레 쿼리
# query_w = db.obesity_total.explain("executionStats").aggregate([
#     {'$match':{
#         'BMI':{'$lt':18.5}
#         }
#     },
#     {'$group':{
#         '_id':'$성별','avg_waist':{'$avg':'$허리둘레'}
#         }
#     }
# ])
