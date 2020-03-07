import requests


response = requests.delete(
'http://pythonmc.free.beeceptor.com/usuarios?id=1')


if response.status_code == 200:
    print(response.json())
