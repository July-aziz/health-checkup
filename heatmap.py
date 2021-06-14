import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('./data/국민건강보험공단_건강검진정보_20191231.txt')
# df.info()
columns1 = [
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

columns2 = [
    "BMI",
    "허리둘레",
    "수축기 혈압",
    "이완기 혈압",
    "음주여부"]

df[['음주여부']] = df[['음주여부']].fillna(0)
df = df.assign(BMI=lambda x: 10000*x['체중(5Kg 단위)']/(x['신장(5Cm단위)']*x['신장(5Cm단위)']))
df_small1 = df[columns1]
# df_small.info()
df_corr1 = df_small1.corr()
df_corr_round1 = df_corr1.round(2)

fig1 = ff.create_annotated_heatmap(
    z=df_corr_round1.to_numpy(),
    x=df_corr1.columns.tolist(),
    y=df_corr1.columns.tolist(),
    colorscale='blues',
    zmax=1, zmin=-1,
    showscale=True,
    reversescale=False,
    hoverongaps=True
)

fig1.update_layout(
    title=dict(
        text='검강검진 데이터 상관분석',
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

fig1.show()

df_small2 = df[columns2]
# df_small.info()
df_corr2 = df_small2.corr()
df_corr_round2 = df_corr2.round(2)

fig2 = ff.create_annotated_heatmap(
    z=df_corr_round2.to_numpy(),
    x=df_corr2.columns.tolist(),
    y=df_corr2.columns.tolist(),
    colorscale='blues',
    zmax=1, zmin=-1,
    showscale=True,
    reversescale=False,
    hoverongaps=True
)

fig2.update_layout(
    title=dict(
        text='검강검진 데이터 상관분석',
        x=0.5,
        font=dict(
            size=20,
        ),
    ),
    paper_bgcolor='rgb(255, 255, 255)',
    plot_bgcolor='rgb(245, 255, 245)',
    width=500,
    height=500,
)

fig2.show()
