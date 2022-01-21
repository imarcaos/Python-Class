# Calculator BMI (Body Mass Index) ou Calculadore IMC (Índice de Massa Corporal)
# Peso KG , Altura CM
#21/01/2022

altura = float(input("Qual é a sua Altura em cm ? "))
peso = float(input("Qual é o seu peso em kg ? "))

imc = peso / (altura/100)**2 
# Para formatar as casas decimais utilizar após a variável :.2f
#print(imc)
print("\n-----------------------------------------------------------------------")

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Magreza\n")
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Normal\n")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Sobrepeso\n")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Obesidade\n")
else:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Obesidade Grave\n")
