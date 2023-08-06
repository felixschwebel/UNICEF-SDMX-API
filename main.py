import requests

endpoint = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest"

dataflow_add = "/dataflow/all/all/latest"
dataflow_params = {
    "format": "sdmx-json",
    "detail": "full",
    "reference": "none",
}

response = requests.get(url=endpoint+dataflow_add, params=dataflow_params)
text = response.json()
print(response.status_code)
