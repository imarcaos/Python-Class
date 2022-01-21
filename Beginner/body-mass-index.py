# Calculator BMI (Body Mass Index) ou Calculadore IMC (Índice de Massa Corporal)
# Peso KG , Altura CM
# 21/01/2022

print("\n-----------------------------------------------------------------------")
print("CALCULADORA DE IMC - ÍNDICE DE MASSA CORPORAL")
altura = float(input("\nQual é a sua Altura em cm ? "))
peso = float(input("Qual é o seu peso em kg ? "))

imc = peso / (altura/100)**2 

print("\n-----------------------------------------------------------------------")
print("# MENOR QUE 18,5     MAGREZA             - 0")
print("# ENTRE 18,5 E 24.9  NORMAL              - 0")
print("# ENTRE 25   E 29.9  SOBREPESO           - I")
print("# ENTRE 30   E 39.9  OBESIDADE           - II")
print("# MAIOR QUE 40       OBESIDADE  GRAVE    - III")
print("-----------------------------------------------------------------------")

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Magreza\n") # Para formatar as casas decimais utilizar após a variável :.2f
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Normal\n")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Sobrepeso\n")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Obesidade\n")
else:
    print(f"Seu IMC é de {imc:.2f} , e é classificado como Obesidade Grave\n")
