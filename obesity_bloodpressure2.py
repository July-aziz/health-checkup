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
  "x": ["56~75", "76~95","96~115","116~135","136~155","156~175","176~195","196~215","216~235","236~255","256~275"],
  "y": [20.8943,21.0073,22.6349,24.4099,25.4323,25.7425,25.8368,26.0411,27.4928,25.9388,19.0250],
  "marker": {
    "line": {
      "color": "rgb(255,051,051)",
      "width": 1.5
    },
    "color": "rgb(255,204,204)"
  },
  "opacity": 0.6,
}
data = [trace1]
layout = {"title": "수축기 혈압 & BMI"}
fig = Figure(data, layout)
# plot_url = py.plot(fig)

fig.show()

#
# # 시각화 - 이완기 혈압 & BMI
# trace1 = {
#   "type": "bar",
#   "x": ["26~45", "46~65","66~85","86~105","106~125","126~145","146~165","166~185","186~205"],
#   "y": [21.5806,22.2828,24.0245,25.4853,26.7363,27.4674,27.8312,28.4912,23.8751],
#   "marker": {
#     "line": {
#       "color": "rgb(8,48,107)",
#       "width": 1.5
#     },
#     "color": "rgb(158,202,225)"
#   },
#   "opacity": 0.6,
# }
# data = [trace1]
# layout = {"title": "이완기 혈압 & BMI"}
# fig = Figure(data, layout)
# # plot_url = py.plot(fig)
#
# fig.show()
#
# # 시각화 - 수축기 혈압 & 이완기 혈압
# trace1 = {
#   "type": "bar",
#   "x": ["26~45", "46~65","66~85","86~105","106~125","126~145","146~165","166~185","186~205"],
#   "y": [95.2374,107.0105,122.0064,138.7370,161.2944,186.0389,205.1481,213.8,220],
#   "marker": {
#     "line": {
#       "color": "rgb(255,102,051)",
#       "width": 1.5
#     },
#     "color": "rgb(255,255,153)"
#   },
#   "opacity": 0.6,
# }
# data = [trace1]
# layout = {"title": "이완기 혈압 & 수축기 혈압"}
# fig = Figure(data, layout)
# # plot_url = py.plot(fig)
#
# fig.show()