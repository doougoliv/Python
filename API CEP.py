
import requests
import json

lista_cep = ['01009905']
lista_enderecos = []

for cep in lista_cep:
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    req = requests.get(url, timeout=3)

    endereco = req.json()

    lista_enderecos.append([endereco["cep"], endereco["logradouro"], endereco["uf"], endereco["bairro"]])

    print(endereco)

for item in lista_enderecos:
    print(item)
