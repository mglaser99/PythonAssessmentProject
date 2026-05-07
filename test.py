import requests
import json

url = "http://127.0.0.1:8000/"

inputs = [
    {
      "reference": "Higgs boson in particle physics",
      "other": ["Best soup recipes", "Basel activities", "Particle physics at CERN"]
    },
]

for body in inputs:
    result = requests.post(url, json=body)
    print(f"Reference: {body['reference']}\nMost similar: {json.loads(result.text)['top_result']}\n\n")

