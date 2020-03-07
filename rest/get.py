#!/usr/bin/env python3
import requests

cep = str(input('Entre com o CEP (00000-000):'))

url1 = f'https://viacep.com.br/ws/{cep}/json/'
url2 = 'https://viacep.com.br/ws/{0}/json/'.format(cep)
url3 = 'https://viacep.com.br/ws/{cep}/json/'.format(cep=cep)

response = requests.get(url1)

if response.status_code == 200:
   dados = response.json()
   print('Logradouro: {0} \n Bairro: {1}'. format(dados['logradouro'],dados['bairro']))

elif response.status_code == 400:
    print('O cep informado é invalido')
else:
    print(response.status_code)
    
