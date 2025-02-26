import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = requisicao.json()
print ('Moeda: ' + cotacao['USD']['name'])
