import chart_studio.plotly as py
from plotly.graph_objs import Scatter, Bar, Figure, Data, Area, Histogram
from pymongo import MongoClient
import pymongo

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.health
obesity_bloodpressure = db.obesity_total

# 시각화 - 수축기 혈압 & 이완기 혈압
trace1 = {
  "mode": "lines+markers",
  "name": "이완기 혈압 & 수축기 혈압",
  "type": "scatter",
  "x": ["26~45", "46~65","66~85","86~105","106~125","126~145","146~165","166~185","186~205"],
  "y": [95.2374,107.0105,122.0064,138.7370,161.2944,186.0389,205.1481,213.8,220],
  "marker": {
    "size": 12
  },
}

data = [trace1]
layout = {"title": "이완기 혈압 & 수축기 혈압",
          "xaxis.title": "이완기 혈압",
          "yaxis.title": "수축기 혈압",
          "showlegend": True,
          "bargroupgap": 0,
          "boxgroupgap": 0.3,
          "plot_bgcolor": "#c8c8f8",
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
