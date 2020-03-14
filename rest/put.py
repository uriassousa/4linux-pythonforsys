import requests

data = {"nome": "Krishnamurti"}
response = requests.put(
'http://pythonmc.free.beeceptor.com/usuarios', json=data)


if response.status_code == 200:
    print(response.json())
