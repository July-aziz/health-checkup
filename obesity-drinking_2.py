from pymongo import MongoClient
import plotly.graph_objects as go

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.healthCheckup
obesity_drinking = db.obesity_drinking

Figure2 = go.Figure()

x = ['저체중', '정상체중', '과체중', '경도비만', '중정도비만', '고도비만', ]
y_drinking_true = []
y_drinking_false = []
cnt_1 = 0
cnt_0 = 0
for data in healthCheckup.find():
    if data['음주여부'] == "1":
        cnt_1 = cnt_1 + 1
    else:
        cnt_0 = cnt_0 + 1

query1 = obesity_drinking.aggregate([
    {'$match': {
        'BMI': {'$lt': 18.5}
    }
    },
    {'$group': {
        '_id': '$음주여부',
        'count': {'$sum': 1}
    }
    }
])
query2 = obesity_drinking.aggregate([
    {'$match': {
        '$and': [{'BMI': {'$gte': 18.5}}, {'BMI': {'$lt': 23}}],
    }
    },
    {'$group': {
        '_id': '$음주여부',
        'count': {'$sum': 1}
    }
    }
])
query3 = obesity_drinking.aggregate([
    {'$match': {
        '$and': [{'BMI': {'$gte': 23}}, {'BMI': {'$lt': 25}}],
    }
    },
    {'$group': {
        '_id': '$음주여부',
        'count': {'$sum': 1}
    }
    }
])
query4 = obesity_drinking.aggregate([
    {'$match': {
        '$and': [{'BMI': {'$gte': 25}}, {'BMI': {'$lt': 30}}],
    }
    },
    {'$group': {
        '_id': '$음주여부',
        'count': {'$sum': 1}
    }
    }
])
query5 = obesity_drinking.aggregate([
    {'$match': {
        '$and': [{'BMI': {'$gte': 30}}, {'BMI': {'$lt': 35}}],
    }
    },
    {'$group': {
        '_id': '$음주여부',
        'count': {'$sum': 1}
    }
    }
])
query6 = obesity_drinking.aggregate([
    {'$match': {
        'BMI': {'$gte': 35}
    }
    },
    {'$group': {
        '_id': '$음주여부',
        'count': {'$sum': 1}
    }
    }
])
# print(query2.__dict__['_CommandCursor__data'])
# drinking_by_bmi = query1.__dict__
# print(drinking_by_bmi['_CommandCursor__data'])
# 저체중 18.5 정상체중 23 과체중 25 경도비만 30 중정도비만 35 고도비만

y_drinking_true.append(round(query1.__dict__['_CommandCursor__data'][0]['count'] / cnt_1 * 100, 2))
y_drinking_false.append(round(query1.__dict__['_CommandCursor__data'][1]['count'] / cnt_0 * 100, 2))
y_drinking_true.append(round(query2.__dict__['_CommandCursor__data'][0]['count'] / cnt_1 * 100, 2))
y_drinking_false.append(round(query2.__dict__['_CommandCursor__data'][1]['count'] / cnt_0 * 100, 2))
y_drinking_true.append(round(query3.__dict__['_CommandCursor__data'][0]['count'] / cnt_1 * 100, 2))
y_drinking_false.append(round(query3.__dict__['_CommandCursor__data'][1]['count'] / cnt_0 * 100, 2))
y_drinking_true.append(round(query4.__dict__['_CommandCursor__data'][0]['count'] / cnt_1 * 100, 2))
y_drinking_false.append(round(query4.__dict__['_CommandCursor__data'][1]['count'] / cnt_0 * 100, 2))
y_drinking_true.append(round(query5.__dict__['_CommandCursor__data'][0]['count'] / cnt_1 * 100, 2))
y_drinking_false.append(round(query5.__dict__['_CommandCursor__data'][1]['count'] / cnt_0 * 100, 2))
y_drinking_true.append(round(query6.__dict__['_CommandCursor__data'][0]['count'] / cnt_1 * 100, 2))
y_drinking_false.append(round(query6.__dict__['_CommandCursor__data'][1]['count'] / cnt_0 * 100, 2))

Figure2 = go.Figure(data=[
    go.Bar(
        name='음주함',
        x=x,
        y=y_drinking_true,
        text=y_drinking_true,
        textposition='outside',
        marker_color='rgb(252, 235, 170)',
    ),
    go.Bar(
        name='음주안함',
        x=x,
        y=y_drinking_false,
        text=y_drinking_false,
        textposition='outside',
        marker_color='rgb(252, 230, 150)',
    )
])
Figure2.update_layout(
    title=dict(
        text='음주여부별 BMI비율 비교',
        x=0.5,
        font=dict(
            size=20,
        ),
    ),
    xaxis=dict(
        gridcolor='gray',
        gridwidth=1,
    ),
    yaxis=dict(
        title='인구비율(%)',
        gridcolor='gray',
        gridwidth=1,
    ),
    paper_bgcolor='rgb(255, 255, 255)',
    plot_bgcolor='rgb(255, 252, 230)',
    width=1200,
    height=600,
    legend=dict(
        bordercolor='black',
        borderwidth=1,
        orientation="v",
        yanchor="top",
        x=0.93,
        y=0.95,
        xanchor="center",
    ),
)

Figure2.show()
