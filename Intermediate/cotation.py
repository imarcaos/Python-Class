# Retorna a cotação de algumas moedas, programa somente para testar o Tkinter - desenho de janelas GUI
# 22/01/2022

import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/EUR-USD,BTC-USD")

    requisicao_dic =   requisicao.json()

    cotacao_dolar = requisicao_dic['EURUSD']['bid']
    cotacao_btc = requisicao_dic['BTCUSD']['bid']


    texto = f'''
    Dólar/EUR: {cotacao_dolar}
    BTC/Dólar: {cotacao_btc}'''

    print(texto)

#pegar_cotacoes()

janela = Tk() # cria a janela
janela.title("Cotação Atual das Moedas")

texto_orientacao = Label(janela, text="Clique no Botão para Atualizar as Cotações das Moedas")
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="ATUALIZAR COTAÇÕES", command=pegar_cotacoes)
botao.grid(column=0, row=1)

janela.mainloop() # mantém a janela aberta e deve estar sempre em último