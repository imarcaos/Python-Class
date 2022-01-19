#Factorial Number Calc
num = int(input("Digite um número inteiro positivo para fazer o fatorial: "))
resultado = 1
nTemp = 1

if num < 0:
    #Colocar outro while
    print("! Por Favor, digite um número positivo maior que 0 !")
elif num == 1 and num == 0:
    print("O Fatorial de ", num, " é -> 1")
else:
    while( nTemp <= num):    
        resultado *= nTemp
        nTemp += 1

print("O Fatorial de ", num, " é -> ", resultado)

