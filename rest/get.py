#!/usr/bin/env python3
import requests

response = requests.get('https://viacep.com.br/ws/06864-130/json/')

if response.status_code == 200:
    print(response.json())
    
