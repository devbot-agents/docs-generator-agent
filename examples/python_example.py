#!/usr/bin/env python3
# Exemplo de como chamar o endpoint do agente usando Python

import requests
import json

url = "http://localhost:8000/api/v1/execute"
data = {
    "type": "exemplo_type",
    "properties": {
        "name": {
            "type": "exemplo_type"
        },
        "description": {
            "type": "exemplo_type"
        },
        "input_schema": {
            "type": "exemplo_type"
        },
        "output_schema": {
            "type": "exemplo_type"
        },
        "endpoint_url": {
            "type": "exemplo_type"
        }
    }
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=2))
