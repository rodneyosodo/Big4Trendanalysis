import requests
import os
from pprint import pprint
import pandas as pd
import time
import env

start = time.time()
key = env.azure_key
text_analytics_base_url = "https://uksouth.api.cognitive.microsoft.com/text/analytics/v2.0/"
sentiment_api_url = text_analytics_base_url + "sentiment"
headers = {"Ocp-Apim-Subscription-Key": key}

data = pd.read_csv("Data/Crosscheck.csv")
data['Azuretarget'] = 0
target = []
counter = 0
for i in range(0, len(data), 1):
	counter = counter + 1
	documents = {'documents' : [
	  {'id': '1', 'language': 'en', 'text': data["text"][i]}
	]}
	respose = requests.post(sentiment_api_url, headers=headers, json=documents)
	sentiment = respose.json()
	target.append(sentiment.get('documents')[0].get("score"))
	if counter%100 == 0:
		print(counter, "\n")

end = time.time()
time_diff = end - start
data['Azuretarget'] = target
pprint("Finished\nIterations: {}\nLength of data frame: {}\nIt took {} seconds".format(counter, len(data), time_diff))