import requests

nome = input('Informe o nome: ')

if len(nome) <= 3:
    print('Nome inválido')
    exit()
    
data = {"nome": "nome"}

response = requests.post('https://pythonmc.free.beeceptor.com/usuarios', json=data)
    
if response.status_code == 200:
    print(response.json())
    data['criacao'] = datetime.now().strftime('%Y-%m-%d')
    print(data)
