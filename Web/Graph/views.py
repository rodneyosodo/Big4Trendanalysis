from django.shortcuts import render
from django.http import HttpResponse

# Include the fusioncharts.py file which has required functions to embed the charts in html page
from fusioncharts import FusionCharts
from fusioncharts import FusionTable
from fusioncharts import TimeSeries
import requests

# Loading Data and schema from a Static JSON String url
# The chart method is defined to load chart data from an JSON string.

def chart(request):

   data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/plotting-multiple-series-on-time-axis-data.json').text
   schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-multiple-series-on-time-axis-schema.json').text

   fusionTable = FusionTable(schema, data)
   timeSeries = TimeSeries(fusionTable)
   
   timeSeries.AddAttribute('chart', '{}');
   timeSeries.AddAttribute('caption', '{"text": "Sales Analysis"}');
   timeSeries.AddAttribute('subcaption', '{"text": "Grocery & Footwear"}');
   timeSeries.AddAttribute('series', '"Type"');
   timeSeries.AddAttribute('yaxis', '[{"plot": "Sales Value","title": "Sale Value","format": {"prefix": "$"}}]');

   # Create an object for the chart using the FusionCharts class constructor
   fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)

   # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
   return  render(request, 'index.html', {'output' : fcChart.render()})

"""
from django.shortcuts import render
from django.http import HttpResponse
from fusioncharts import FusionCharts

def chart(request):
      chartObj = FusionCharts(
         'realtimeline',
         'ex1',
         '600',
         '400',
         'chart-1',
         'json',
         ""#"{
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
}""#")

      return render(request, 'fusioncharts-html-template.html', {'output': chartObj.render()})
"""