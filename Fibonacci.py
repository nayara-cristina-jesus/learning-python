### Sequência de Fibonacci

# Valores iniciais: fib_1 = 1 e fib_2 = 1
# Fórmula: fib_n = fib_n-1 + fib_n-2
# Exemplo, 10 primeiros termos da sequência: 0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

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
