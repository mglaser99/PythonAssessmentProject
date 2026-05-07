import requests
import json

url = "http://127.0.0.1:8000/"

inputs = [
    {
      "reference": "Higgs boson in particle physics",
      "other": ["Best soup recipes", "Basel activities", "Particle physics at CERN"]
    },
    {
      "reference": "Climate change effects",
      "other": [
        "Climate change effects",
        "Ocean photography",
        "Laptop buying guide"
      ]
    },
    {
      "reference": "Renewable energy sources",
      "other": [
        "Solar panel installation"
      ]
    },
    {
      "reference": "Artificial intelligence",
      "other": []
    },
    {
      "reference": "Artificial intelligence",
      "other": [""]
    },
    {
      "reference": "",
      "other": [
        "Space exploration",
        "Cooking pasta"
      ]
    }
]

for body in inputs:
    result = requests.post(url, json=body)
    print(f"Reference: {body['reference']}\nMost similar: {json.loads(result.text)['top_result']}\n\n")

