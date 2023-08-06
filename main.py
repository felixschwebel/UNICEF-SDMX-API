import requests

endpoint = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest"

dataflow_add = "/dataflow/all/all/latest"
dataflow_params = {
    "format": "sdmx-json",
    "detail": "full",
    "reference": "none",
}

response = requests.get(url=endpoint+dataflow_add, params=dataflow_params)
file = response.json()
print(response.status_code)

dataflows = file['data']['dataflows']
for item in dataflows:
    print(f"name: {item['name']} - id: {item['id']}")