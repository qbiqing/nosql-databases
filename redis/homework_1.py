#no-sql homework 1
#Biqing Qiu, bq2134
#install requests using pip install requests

import requests

url = "https://api.nasa.gov/planetary/apod?api_key=x58gR1ZBQS5cbOJmkTCHbypN2UnR44DB8E6pabJG"
param = {'date':'1996-03-26', 'hd': True}
response = requests.get(url, params = param)
data = response.json()
print(data['url'])
