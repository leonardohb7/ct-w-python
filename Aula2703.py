mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Toda vez que next é usado ele aponta pro proximo indice

# for <referência> in <sequência>:
#   <bloco de código>

Lista = ['Dark Side of the Moon', 'Animals', 'The Wall']

for album in Lista:
    print(album)

lista = list(range(0, 30)) #list cria um array com todos os valores desse intervalo
print(lista)

for i in lista:
    print(i)

for i in range(0, 30): #range vai do index inicial, até o final -1, ou seja de 0 a 29 (30-1)
    print(i)

s='the quick brown fox jumps over the lazy dog'

if 'a'in s:             #in verifica se o valor esta contido em outro dado
    print('contido')

if '6' not in s:
    print('não está contido')

for i in range(0, 30):
    if i == 15:
        break  #break interrompe o loop inteiro (ate se tiver else no for)
    print(i)

for i in range(0, 30):
    if i%2 != 0:
        continue #continue pula para a proxima iteração
    print(i)

for i in range(0, 30):
    if i == 15:
        print('Encontrei')
    break
else:
    print('Não Encontrei') #somente o python tem else no loop while e for

L=['a', 'e', 'i', 'o', 'u']
for i,letra in enumerate(L): #enumerate percorre a lista e retorna indice e valor
    print(i,letra)

lista = [value ** 2 for value in range(1, 11)] #list comprehensions. voce fazer uma lista, com um for na declaracao
print(lista)

pares = [i for i in range(0, 101) if i % 2 == 0]
print(pares)


