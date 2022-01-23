# Como utilizar api, request, json
# site de api pública utilizado: https://docs.awesomeapi.com.br/api-de-moedas
# vou deixar todos os comentários passo a passo para uma eventual pesquisa
# 23/01/2022

import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/EUR-USD,BTC-USD,ETH-USD")
#print(cotacoes) # nesta forma ela recebe a informação <Response [200]>,  que signifca informação recebida ok
cotacoes = cotacoes.json() # faz a conversão do formato json para um formato texto do python
#cotacao_dolar = cotacoes['EURUSD'] # retorna toda informação do EUR-USD, ao imprimir podemos escolher uma especifica, no caso 'bid'
cotacao_dolar = cotacoes['EURUSD']['bid'] # retorna o valor cotação atual do EUR-USD
cotacao_btc = cotacoes['BTCUSD']['bid']
cotacao_eth = cotacoes['ETHUSD']['bid']
#print(cotacoes) # imprime o toda informação recebida
#print(cotacao_dolar) # imprime a cotação do dolar

# aqui entra o estudo de f-strings
texto= f'''
    Dólar-Euro: {cotacao_dolar}
    BTC-USD   : {cotacao_btc}
    ETH-USD   : {cotacao_eth}
'''
print(texto)