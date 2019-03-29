from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from fusioncharts import FusionCharts

def chart(request):
      chartObj = FusionCharts(
         'realtimeline',
         'ex1',
         '700',
         '400',
         'chart-1',
         'json',
         """{
  "chart": {
    "caption": "Bitcoin Price Ticker",
    "subcaption": "Jan 31, 2019",
    "numberprefix": "$",
    "numdisplaysets": "10",
    "labeldisplay": "rotate",
    "showrealtimevalue": "0",
    "theme": "fusion",
    "plottooltext": "$label<br>Price: <b>$dataValue</b>",
    "setadaptiveymin": "1"
  },
  "categories": [
    {
      "category": [
        {
          "label": "15:8:29"
        },
        {
          "label": "15:8:30"
        },
        {
          "label": "15:8:31"
        }
      ]
    }
  ],
  "dataset": [
    {
      "data": [
        {
          "value": "7358"
        },
        {
          "value": "7361"
        },
        {
          "value": "7362"
        }
      ]
    }
  ]
}""")

      return render(request, 'index.html', {'output': chartObj.render()})
#"""