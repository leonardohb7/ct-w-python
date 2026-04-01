# Strings

text = "This is a string" # É uma cadeia de caracteres
text = 'This is as string' # Pode ser usada com aspas duplas ou simples

texto='''
Este texto
possui mais
de
uma
linha
''' # Também é possível usar aspas triplas. Nesse caso podemos escrever com quebra de linhas

print(texto)

# A concatenação de strings pode ser feita usando os operadores + e *.
name = 'Roberto'
surname = 'Cândido'
space = ' '
full_name = name + space + surname
print(full_name)

name = 'Hello world'
asterisk = '*'
print(asterisk * 3 + name + asterisk * 3)
# asterisk * 3 = asterisk + asterisk + asterisk

numero = 10
texto = f'O valor de {numero} ao quadrado é {10**2}' #Interpolação ou FStrings

s = "Olá, mundo!"
# Tamanho de uma string.
number = len(s)
print(number)

s = "Olá, mundo!"
# Substitui uma substring por alguma outra coisa.
s1 = s.replace("mundo", "inferno")
print(s1)

s = "Olá, mundo!"

# A string s começa com "Olá"?
print(s.startswith("mundo"))

# A string s termina com "mundo!"?
print(s.endswith("mundo!"))

# Quantas ocorrências da palavra "abacate" a string s1 possui?
print(s1.count("abacate"))

# Como "capitalizar" (transformar a primeira letra da primeira palavra em maiúscula).
s = "ordem e progresso"
print(s.capitalize())

# Como verificar se uma string só possui números.
print('12345'.isdigit())
print('12345abc'.isdigit())

# Como verificar se uma string é alfanumérica (só possui letras e números).
print('12345abc'.isalnum())

#String.find: procura uma substring em uma string e retorna o índice:
s = "Pedro, Paulo e Maria"
print(s.find("a"))

#Além disso, ela recebe um argumento adicional que especifica o índice pelo qual ela deve começar sua procura:
print(s.find("a", 10))

#Ord: Retorna o valor decimal (unicode) de um caractere
print(ord('a'))

#chr: retorna o caractere de um valor decimal (unicode).
print(chr(97))

s='Isso é um texto'
print(s.title())
print(s.lower())
print(s.upper())

texto='isso é    '
texto2='   um texto'
print(texto+texto2)

texto=texto.rstrip() #remove os espacos á direita da string
texto2=texto2.lstrip() #removec os espaços á esquerda da string

print(texto+texto2)

texto = 'Isso é um texto besta!'

print(texto[0:7]) #slicing, printa do indice 0 até o 6 (7-1)

print(texto[0:7:2]) # printa de 2 em 2

print(texto[::-1]) #printa de tras pra frente

texto = "Vamos aprender split"

print(texto.split()) # separa usando o separador padrão que é o caracter espaço

texto = "12354@gmail.com"

print(texto.split('@')) #separa usando o separador indicado (@)

lista = ['a', 'b', 'c']

texto = '-'.join(lista) #transforma a lista em uma string, colocando o caractere no meio

print(texto)

# partition() e rpartition() Divide a string em 3 partes: antes, separador, depois.
email = "nome@dominio.com"
usuario, sep, dominio = email.partition("@")
print(usuario, sep, dominio)



#find(), rfind() e index()
#Localizam substrings:
texto = "banana"
print(texto.find("na")) # 2
print(texto.rfind("na")) # 4 (procura da direita pra esquerda)
print(texto.index("n")) # 2

# zfill() e rjust(), ljust() Formatar número/palavra com preenchimento:
print("42".zfill(5)) # '00042'
print("42".rjust(5, "*")) # '***42'
print("42".ljust(5, "-")) # '42---'


#translate() com str.maketrans() Permite substituições múltiplas de caracteres:

tabela = str.maketrans("aeiou", "12345")

print("substituir vogais".translate(tabela))

#casefold() — Para comparação insensível a maiúsculas/minúsculas (melhor que lower())
print("straße".casefold() == "STRASSE".casefold()) # True (útil para alemão, francês etc.)

#replace() com contagem
texto = "aaaabbbbcccc"
novo = texto.replace("a", "x", 2) # 'xxaabbbbcccc'
print(novo)