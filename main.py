import requests

URL = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/dataflow/all/all/latest/?format=sdmx-json&detail=full&references=none"

response = requests.get(URL).json()

for i in response:
    print(i)
