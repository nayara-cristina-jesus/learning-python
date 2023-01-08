# Calculo do IMC

'''
------------------------------------  
  IMC (kg/m²)	 - Classificação
------------------------------------  
menor que 18,5 - Magreza
de 18,5 a 24,9 - Peso normal
de 25,0 a 29,9 - Sobrepeso
de 30,0 a 34,9 - Obesidade grau I
de 35,0 a 40,0 - Obesidade grau II
maior que 40,0 - Obesidade grau III
'''

print("Calculo do IMC")

# Entrada de dados
altura = float(input("\nInforme a sua altura (m): "))
peso = float(input("\nInforme o seu peso (kg): "))

# Calculando IMC
imc = (peso/altura)/2

# Saida de dados
print("\nIMC: %.2f" %imc)

# Classificando IMC
if imc < 18.5:
  print("\nMagreza")
elif imc < 24.9:
  print("\nPeso normal")
elif imc < 29.9:
  print("\nSobrepeso")
elif imc < 34.9:
  print("\nObesidade grau I")
elif imc < 40.0:
  print("\nObesidade grau II") 
else:
  print("\nObesidade grau III") 

print()
