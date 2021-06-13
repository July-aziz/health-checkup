import chart_studio.plotly as py
from plotly.graph_objs import Scatter, Bar, Figure, Data, Area, Histogram
from pymongo import MongoClient
import pymongo

client = MongoClient('localhost', 27017)
db = client.july
healthCheckup = db.health
obesity_bloodpressure = db.obesity_bloodpressure

# 시각화 - 수축기 혈압 & BMI
trace1 = {
  "type": "bar",
  "name": "수축기 혈압 & BMI",
  "x": ["56~75", "76~95","96~115","116~135","136~155","156~175","176~195","196~215","216~235","236~255","256~275"],
  "y": [20.8943,21.0073,22.6349,24.4099,25.4323,25.7425,25.8368,26.0411,27.4928,25.9388,19.0250],
  "marker": {
    "line": {
      "color": "rgb(255,051,051)",
      "width": 1.5
    },
    "color": "rgb(254,194,194)"
  },
  "opacity": 0.6,
}
data = [trace1]
layout = {"title": "수축기 혈압 & BMI",
          "xaxis.title": "수축기 혈압",
          "yaxis.title": "BMI",
          "showlegend": True,
          "bargroupgap": 0,
          "boxgroupgap": 0.3,
          "plot_bgcolor": "#fef0f0",
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

fig.show()
