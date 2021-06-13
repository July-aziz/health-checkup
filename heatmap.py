from pymongo import MongoClient
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import seaborn

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.healthCheckup
obesity_drinking = db.obesity_drinking

df = pd.read_csv('./data/국민건강보험공단_건강검진정보_20191231.txt')
# df.info()
columns = [
    "연령대 코드(5세단위)",
    "BMI",
    "신장(5Cm단위)",
    "체중(5Kg 단위)",
    "허리둘레",
    "시력(좌)",
    "시력(우)",
    "청력(좌)",
    "청력(우)",
    "수축기 혈압",
    "이완기 혈압",
    "식전혈당(공복혈당)",
    "총 콜레스테롤",
    "트리글리세라이드",
    "HDL 콜레스테롤",
    "LDL 콜레스테롤",
    "혈색소",
    "요단백",
    "혈청크레아티닌",
    "(혈청지오티)AST",
    "(혈청지오티)ALT",
    "감마 지티피",
    "흡연상태",
    "음주여부"]

df[['음주여부']] = df[['음주여부']].fillna(0)
df = df.assign(BMI=lambda x: 10000*x['체중(5Kg 단위)']/(x['신장(5Cm단위)']*x['신장(5Cm단위)']))
df_small = df[columns]
# df_small.info()
df_corr = df_small.corr()
df_corr_round = df_corr.round(2)

fig = ff.create_annotated_heatmap(
    z=df_corr_round.to_numpy(),
    x=df_corr.columns.tolist(),
    y=df_corr.columns.tolist(),
    colorscale='blues',
    zmax=1, zmin=-1,
    showscale=True,
    reversescale=False,
    hoverongaps=True
)

fig.update_layout(
    title=dict(
        text='검강검진 결과 상관분석',
        x=0.5,
        font=dict(
            size=20,
        ),
    ),
    paper_bgcolor='rgb(255, 255, 255)',
    plot_bgcolor='rgb(245, 255, 245)',
    width=1050,
    height=1050,
)

fig.show()
