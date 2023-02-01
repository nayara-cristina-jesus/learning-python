#Verificar se um número é ou não primo

num = int(input("Número: "))
multiplo = 0

print("")
for contagem in range(2, num):
  if(num % contagem == 0):
    print(num,"é múltiplo de", contagem)
    multiplo = multiplo + 1
    
if (multiplo == 0):
  print(num,"é um número primo.")
else:
  print("\n Então",num,"não é um número primo.")
