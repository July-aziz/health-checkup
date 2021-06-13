from pymongo import MongoClient
import pprint
import plotly
import plotly.graph_objects as go
import time  # 인덱싱 전후 시간 비교를 위해서

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.health
obesity = db.obesity_waist
# obesity = db.obesity_total

start = time.time()  # 시작 시간 저장

# 저체중 18.5 정상체중 23 과체중 25 경도비만 30 중정도비만 35 고도비만

#################################################################
# bmi별 허리둘레평균 구하는 쿼리

# 저체중 평균 허리둘레
query1 = obesity.aggregate([
    {'$match': {
        'BMI': {'$lt': 18.5}
    }},
    {'$group': {
        '_id': '$성별', 'avg_waist': {'$avg': '$허리둘레'}
    }}
])
for x in query1:
    print(x)

# 정상체중 평균 허리둘레
query2 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 18.5, '$lt': 23.0}
    }},
    {'$group': {
        '_id': '$성별', 'avg_waist': {'$avg': '$허리둘레'}
    }}
])
for x in query2:
    print(x)

# 과체중 평균 허리둘레
query3 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 23.0, '$lt': 25.0}
    }},
    {'$group': {
        '_id': '$성별', 'avg_waist': {'$avg': '$허리둘레'}
    }}
])
for x in query3:
    print(x)

# 경도비만 평균 허리둘레
query4 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 25.0, '$lt': 30.0}
    }},
    {'$group': {
        '_id': '$성별', 'avg_waist': {'$avg': '$허리둘레'}
    }}
])
for x in query4:
    print(x)

# 중정도비만 평균 허리둘레
query5 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 30.0, '$lt': 35.0}
    }},
    {'$group': {
        '_id': '$성별', 'avg_waist': {'$avg': '$허리둘레'}
    }}
])
for x in query5:
    print(x)

# 고도비만 평균 허리둘레
query6 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 35.0}
    }},
    {'$group': {
        '_id': '$성별', 'avg_waist': {'$avg': '$허리둘레'}
    }}
])
for x in query6:
    print(x)

################################################################
# 성별,bmi별 평균 허리둘레 기준으로 낮고 큼의 비율구하는 쿼리

# 성별별로 평균 허리둘레
query7 = obesity.aggregate([
    {'$group': {
        '_id': '$성별', 'avg_waist': {'$avg': '$허리둘레'}
    }}
])
for x in query7:
    print(x)

# 저체중에서 평균보다 낮은 사람(여성)
query8 = obesity.aggregate([
    {'$match': {
        'BMI': {'$lt': 18.5},
        '성별': '여',
        '허리둘레': {'$lte': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균이하인 사람수': {'$sum': 1}
    }}
])
for x in query8:
    print(x)

# 저체중에서 평균보다 높은 사람(여성)
query9 = obesity.aggregate([
    {'$match': {
        'BMI': {'$lt': 18.5},
        '성별': '여',
        '허리둘레': {'$gt': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균초과인 사람수': {'$sum': 1}
    }}
])
for x in query9:
    print(x)

# 정상체중에서 평균보다 낮은 사람(여성)
query10 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 18.5, '$lt': 23.0},
        '성별': '여',
        '허리둘레': {'$lte': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균이하인 사람수': {'$sum': 1}
    }}
])
for x in query10:
    print(x)

# 정상체중에서 평균보다 높은 사람(여성)
query11 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 18.5, '$lt': 23.0},
        '성별': '여',
        '허리둘레': {'$gt': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균초과인 사람수': {'$sum': 1}
    }}
])
for x in query11:
    print(x)

# 과체중에서 평균보다 낮은 사람(여성)
query12 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 23.0, '$lt': 25.0},
        '성별': '여',
        '허리둘레': {'$lte': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균이하인 사람수': {'$sum': 1}
    }}
])
for x in query12:
    print(x)

# 과체중에서 평균보다 높은 사람(여성)
query13 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 23.0, '$lt': 25.0},
        '성별': '여',
        '허리둘레': {'$gt': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균초과인 사람수': {'$sum': 1}
    }}
])
for x in query13:
    print(x)

# 경도비만에서 평균보다 낮은 사람(여성)
query14 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 25.0, '$lt': 30.0},
        '성별': '여',
        '허리둘레': {'$lte': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균이하인 사람수': {'$sum': 1}
    }}
])
for x in query14:
    print(x)

# 경도비만에서 평균보다 높은 사람(여성)
query15 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 25.0, '$lt': 30.0},
        '성별': '여',
        '허리둘레': {'$gt': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균초과인 사람수': {'$sum': 1}
    }}
])
for x in query15:
    print(x)

# 중정도비만에서 평균보다 낮은 사람(여성)
query16 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 30.0, '$lt': 35.0},
        '성별': '여',
        '허리둘레': {'$lte': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균이하인 사람수': {'$sum': 1}
    }}
])
for x in query16:
    print(x)

# 중정도비만에서 평균보다 높은 사람(여성)
query17 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 30.0, '$lt': 35.0},
        '성별': '여',
        '허리둘레': {'$gt': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균초과인 사람수': {'$sum': 1}
    }}
])
for x in query17:
    print(x)

# 고도비만에서 평균보다 낮은 사람(여성)
query18 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 35.0},
        '성별': '여',
        '허리둘레': {'$lte': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균이하인 사람수': {'$sum': 1}
    }}
])
for x in query18:
    print(x)

# 고도비만에서 평균보다 높은 사람(여성)
query19 = obesity.aggregate([
    {'$match': {
        'BMI': {'$gte': 35.0},
        '성별': '여',
        '허리둘레': {'$gt': 76.76}
    }},
    {'$group': {
        '_id': 'null',
        '평균초과인 사람수': {'$sum': 1}
    }}
])
for x in query19:
    print(x)
#######################################################################################
#저체중에서 평균보다 낮은 사람(남성)
query20 = obesity.aggregate([
    {'$match':{
        'BMI':{'$lt':18.5},
        '성별':'남',
        '허리둘레':{'$lte':85.5}
    }},
        {'$group':{
            '_id':'남자시작',
            '평균이하인 사람수':{'$sum':1}
        }}
        ])
for x in query20:
    print(x)

#저체중에서 평균보다 높은 사람(남성)
query21 = obesity.aggregate([
    {'$match':{
        'BMI':{'$lt':18.5},
        '성별':'남',
        '허리둘레':{'$gt':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균초과인 사람수':{'$sum':1}
        }}
        ])
for x in query21:
    print(x)

#정상체중에서 평균보다 낮은 사람(남성)
query22 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':18.5,'$lt':23.0},
        '성별':'남',
        '허리둘레':{'$lte':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균이하인 사람수':{'$sum':1}
        }}
        ])
for x in query22:
    print(x)

#정상체중에서 평균보다 높은 사람(남성)
query23 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':18.5,'$lt':23.0},
        '성별':'남',
        '허리둘레':{'$gt':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균초과인 사람수':{'$sum':1}
        }}
        ])
for x in query23:
    print(x)

#과체중에서 평균보다 낮은 사람(남성)
query24 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':23.0,'$lt':25.0},
        '성별':'남',
        '허리둘레':{'$lte':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균이하인 사람수':{'$sum':1}
        }}
        ])
for x in query24:
    print(x)

#과체중에서 평균보다 높은 사람(남성)
query25 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':23.0,'$lt':25.0},
        '성별':'남',
        '허리둘레':{'$gt':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균초과인 사람수':{'$sum':1}
        }}
        ])
for x in query25:
    print(x)

#경도비만에서 평균보다 낮은 사람(남성)
query26 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':25.0,'$lt':30.0},
        '성별':'남',
        '허리둘레':{'$lte':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균이하인 사람수':{'$sum':1}
        }}
        ])
for x in query26:
    print(x)

#경도비만에서 평균보다 높은 사람(남성)
query27 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':25.0,'$lt':30.0},
        '성별':'남',
        '허리둘레':{'$gt':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균초과인 사람수':{'$sum':1}
        }}
        ])
for x in query27:
    print(x)


#중정도비만에서 평균보다 낮은 사람(남성)
query28 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':30.0,'$lt':35.0},
        '성별':'남',
        '허리둘레':{'$lte':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균이하인 사람수':{'$sum':1}
        }}
        ])
for x in query28:
    print(x)

#중정도비만에서 평균보다 높은 사람(남성)
query29 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':30.0,'$lt':35.0},
        '성별':'남',
        '허리둘레':{'$gt':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균초과인 사람수':{'$sum':1}
        }}
        ])
for x in query29:
    print(x)


#고도비만에서 평균보다 낮은 사람(남성)
query30 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':35.0},
        '성별':'남',
        '허리둘레':{'$lte':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균이하인 사람수':{'$sum':1}
        }}
        ])
for x in query30:
    print(x)

#고도비만에서 평균보다 높은 사람(남성)
query31 = obesity.aggregate([
    {'$match':{
        'BMI':{'$gte':35.0},
        '성별':'남',
        '허리둘레':{'$gt':85.5}
    }},
        {'$group':{
            '_id':'null',
            '평균초과인 사람수':{'$sum':1}
        }}
        ])
for x in query31:
    print(x)

#################################################################
# 시각화 1. 비만도 별 허리둘레 평균
x = ['저체중', '정상체중', '과체중', '경도비만', '중정도비만', '고도비만']

f1 = [65.20, 72.26, 78.80, 84.42, 93.72, 101.53]  # 여
f2 = [70.53, 78.78, 84.21, 89.81, 100.03, 110.51]  # 남

trace1 = go.Bar(
    x=x,
    y=f1,
    name='여성',
    marker=dict(
        color='rgb(239,192,174)'),
    text=f1,
    textposition='outside'
)

trace2 = go.Bar(
    x=x,
    y=f2,
    name='남성',
    marker=dict(
        color='rgb(180,192,225)'),
    text=f2,
    textposition='outside'
)
data = [trace1, trace2]
layout = go.Layout(
    barmode='group',
    title=dict(
        text='비만도별 허리둘레 평균',
        x=0.5,
        font=dict(
            size=20,
        ),
    ),
    legend=dict(
        bordercolor='black',
        borderwidth=1,
    ),
    width=900,
    height=900,
    plot_bgcolor='rgb(248, 248, 248)',
)
fig = go.Figure(data=data, layout=layout)
fig.show()

# 시각화 2. 성별,bmi별 평균 허리둘레 기준으로 낮고 큼의 비율
# 여성의 경우
f2_1 = [97.81, 77.04, 36.41, 11.42, 0.66, 0.32]  # 평균보다 높은비율
f2_2 = [2.19, 22.96, 63.59, 88.58, 99.34, 99.68]  # 평균보다 낮은비율

fig2 = go.Figure(data=[
    go.Bar(
        name='평균 허리둘레보다 큰 사람 비율',
        x=x,
        y=f2_1,
        marker=dict(
            color='rgb(210,245,250)'),
    ),
    go.Bar(
        name='평균 허리둘레보다 작은 사람 비율',
        x=x,
        y=f2_2,
        marker=dict(
            color='rgb(247,225,225)'),
    )

])
fig2.update_layout(
    barmode='stack',
    legend=dict(
        bordercolor='black',
        borderwidth=1,
    ),
    title=dict(
        text='BMI별 평균 허리둘레 기준보다 낮고 큼의 비율',
        x=0.5,
        font=dict(
            size=20,
        ),
    ),
    width=900,
    height=900,
    plot_bgcolor='rgb(250, 250, 250)',
)
fig2.show()

#남성의 경우
f3_1=[0.67,10.16,39.12,77.57,99.21,99.91] #평균보다 높은비율
f3_2=[99.33,89.84,60.88,22.43,0.79,0.09] #평균보다 낮은비율


fig3=go.Figure(data=[
    go.Bar(name='평균 허리둘레보다 큰 비율',x=x,y=f3_1),
    go.Bar(name='평균 허리둘레보다 작은 비율',x=x,y=f3_2)

])
fig3.update_layout(barmode='stack')
fig3.show()

# waistRatioFigure = go.Figure()
#
# waistRatioFigure.show()


# TODO: 쿼리로 나온 데이터 시각화
# TODO: INDEX하기전 시간 하고난 후 시간 비교하기
