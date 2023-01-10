import time

# Funcao que realiza contagem regressiva, por segundo, de acordo com a entrada informada
def contagem_regressiva (tempo_informado):
  while tempo_informado:
    minuto, segundo = divmod(tempo_informado, 60)
    print('{:02d}:{:02d}'.format(minuto, segundo) + '\n')
    time.sleep(1)
    tempo_informado = tempo_informado - 1
  print('FIM!!!')  

# Entrada de dados
entrada = int(input('\nPor favor, insira um valor inteiro (entre 1 e 60): ')) 
print('\nContagem de ' + str(entrada) + 's iniciando...\n')

# Inicio da execucao da contagem regressiva
contagem_regressiva(entrada)
