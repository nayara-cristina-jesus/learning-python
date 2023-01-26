### Sequência de Fibonacci

num1 = 0
num2 = 1
contagem = 0

try:
  qtde_termos = int(input("\nInforme a quantidade desejada de termos: "))
except ValueError:
    print("\nValor não permitido. \nPor favor, tente novamente.")
else:
  if qtde_termos >= 1:
    if qtde_termos == 1:
      print(num1)
    else:
      while contagem <  qtde_termos:
        print(num1)
        fib = num1 + num2
        num1 = num2
        num2 = fib
        contagem = contagem + 1     
  else:  
    print("\nValor não permitido. \nPor favor, tente novamente.")
