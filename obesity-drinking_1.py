from pymongo import MongoClient
import plotly.graph_objects as go

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.healthCheckup
obesity_drinking = db.obesity_drinking

Figure1 = go.Figure()

query = obesity_drinking.aggregate([
    {'$group': {
        '_id': '$음주여부',
        '평균BMI': {'$avg': '$BMI'}
    }
    }
])
# print(query.__dict__)
# print(vars(query))
bmi_Avg_by_drinking = query.__dict__
# print(bmi_Avg_by_drinking['_CommandCursor__data'][0]['평균BMI'])

x = ['음주함', '음주안함', ]
y = []
y.append(bmi_Avg_by_drinking['_CommandCursor__data'][0]['평균BMI'])
y.append(bmi_Avg_by_drinking['_CommandCursor__data'][1]['평균BMI'])
Figure1 = go.Figure(data=[
    go.Bar(
        name='음주여부',
        x=x,
        y=y,
        text=y,
        textposition='outside',
        marker_color='rgb(100, 100, 100)',
    )
])
Figure1.update_layout(
    title=dict(
        text='음주여부별 BMI 평균 비교',
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
        title='BMI',
        gridcolor='gray',
        gridwidth=1,
        range=(15, 25),
    ),
    paper_bgcolor='rgb(255, 255, 255)',
    plot_bgcolor='rgb(245, 245, 245)',
    width=600,
    height=600,
)

Figure1.show()
