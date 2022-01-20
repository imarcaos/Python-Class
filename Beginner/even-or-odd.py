# Par ou Ímpar - O usuário digita um número e programa responde se é par ou ímpar
# 20/01/2022

continuar = False

while (continuar == False):
    try: # try e except - tratamento de exceções
        print("--------------------------------------------------------------------")
        x = int(input("Quer saber se o número é Par ou Ímpar?, digite um número -> "))

        if x % 2 == 0:
            print(" -> Número Par \n")
        else:
            print(" -> Número Ímpar \n")

        print("/!\ - Para sair do programa digite qualquer caracter não numérico. \n")

    except:
        continuar = True