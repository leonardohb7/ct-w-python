#Try e except evitam o codigo de quebrar com um erro que você sabe que pode aparecer

try:
    print(1/0)

except ZeroDivisionError:
    print('Divisao por zero')



# Exemplo de uso mais profissional, a variável {e} retorna exatamente o erro que seria dado no terminal sem quebrar
def divide(num1, num2):
    return num1/num2
try:
    resultado = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado da divisão: {resultado}")
finally:
    print('Encerrando o programa....')



# Abrir um arquivo no modo de escrita ('w' para escrita, 'a' para adição)
with open('exemplo.txt', 'w') as arquivo:
# Escrever algumas linhas no arquivo
    arquivo.write('Olá, este é um exemplo de escrita em arquivo.\n')
    arquivo.write('                    Python é poderoso e versátil!\n')
    arquivo.write('Fechando o arquivo automaticamente com o bloco "with".                  \n')

# Abrir um arquivo no modo de leitura ('r' para leitura)
with open('exemplo.txt', 'r') as arquivo:
# Ler linhas do arquivo uma a uma
    for linha in arquivo:
        print(linha.strip())
# strip() remove espaços em branco no início e no final da linha

import os
caminho_arquivo = 'exemplo.txt'
if os.path.exists(caminho_arquivo): #verificando se o caminho existe
    print(f'O arquivo {caminho_arquivo} existe.')
else:
    print(f'O arquivo {caminho_arquivo} não existe.')


import os
caminho_arquivo = 'exemplo.txt'
# Verificar se o arquivo existe antes de tentar excluí-lo
if os.path.exists(caminho_arquivo):
    os.remove(caminho_arquivo) #remove o arquivo
    print(f'O arquivo {caminho_arquivo} foi excluído.')
else:
    print(f'O arquivo {caminho_arquivo} não existe.')


#LOGS

import logging

#Criando o arquivo
# Configurando o logger
logging.basicConfig(filename='log.log', level=logging.DEBUG,
format='%(asctime)s - %(levelname)s - %(message)s')
# Realizando as operações de log
logging.debug("Executing program")
logging.debug("Processing data...")
logging.info("Server started successfully.")
logging.warning("Invalid configuration detected.")
logging.error("Failed to connect to the database.")
logging.critical("Unexpected system error occurred. Shutting down.")