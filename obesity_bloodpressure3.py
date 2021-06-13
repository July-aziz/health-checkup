import chart_studio.plotly as py
from plotly.graph_objs import Scatter, Bar, Figure, Data, Area, Histogram
from pymongo import MongoClient
import pymongo

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.health
obesity_bloodpressure = db.obesity_bloodpressure

# 시각화 - 이완기 혈압 & BMI
trace1 = {
  "type": "bar",
  "name": "이완기 혈압 & BMI",
  "x": ["26~45", "46~65","66~85","86~105","106~125","126~145","146~165","166~185","186~205"],
  "y": [21.5806,22.2828,24.0245,25.4853,26.7363,27.4674,27.8312,28.4912,23.8751],
  "marker": {
    "line": {
      "color": "rgb(21,132,187)",
      "width": 1.5
    },
    "color": "rgb(136,206,241)"
  },
  "opacity": 0.6,
}
data = [trace1]
layout = {"title": "이완기 혈압 & BMI",
          "xaxis.title": "이완기 혈압",
          "yaxis.title": "BMI",
          "showlegend": True,
          "bargroupgap": 0,
          "boxgroupgap": 0.3,
          "plot_bgcolor": "#e6f3f9",
          "paper_bgcolor": "#fff",
          "bargap": 0.2,
          "boxgap": 0.3,
          "height": 726,
          "legend": {
            "x": 0.013333333333333334,
            "y": 0.9798534798534798,
            "bgcolor": "#fff",
            "traceorder": "normal",
            "bordercolor": "#000",
            "borderwidth": 2
          }
}

fig = Figure(data, layout)
# plot_url = py.plot(fig)

fig.show()
