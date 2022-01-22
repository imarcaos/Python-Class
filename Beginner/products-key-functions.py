# Função e tratamento de uma lista
# 22/01/2022

produtos = ["ABC123", "abd012", " ABS111", "AbG222"]

texto = "abd012"

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip() # strip com ele vazio retira os espaços vazios
    return texto

texto = "abd012"
texto = tratar_texto(texto)
print(texto)

for i, produto in enumerate(produtos): # i retorna o indíce do produto
    produtos[i] = tratar_texto(produto)

print(produtos)