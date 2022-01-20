# O usuário tem que acertar um número gerado aleatório de 1 a 10, estilo "Dado", caso o usuário
# erre o valor, será respondido se está acima ou abaixo até acertar o número
# 20/01/2022

# para gerar um valor aleatório vou importar uma biblioteca (módulos) pronta para usar a função random

import random

aleaNum = random.randint(1, 10)
#print(aleaNum) # linha para teste
acerto = False

print("Vamos iniciar um jogo estilo 'Dice', a seguir digite um número inteiro entre 1 e 10\n")

while (acerto == False):
    print("--------------------------------------------------------------------")
    x = int(input("Digite um número inteiro entre 1 e 10 para jogar o 'Dice' -> "))
    print("")

    if (x < aleaNum):
        print("-> O número digitado é MENOR que o valor gerado, tente novamente!\n")
        acerto = False
    elif (x > aleaNum):
        print("-> O número digitado é MAIOR que o valor gerado, tente novamente!\n")
        acerto = False
    elif (x == aleaNum):
        print("-> Acertou o número, Parabéns!\n")
        acerto = True

print("Jogo Terminado, Obrigado por participar")
