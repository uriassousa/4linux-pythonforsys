import requests

data = {"nome": "Krishnamurti"}
response = requests.put(
'http://pythonmc.free.beeceptor.com/usuarios', json=data)


if response.status_code == 201:
    print(response.json())
