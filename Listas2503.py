# Listas

lista = [10, 20, 30, 40]

# Cada posição do array (lista) possui um indice, comecando em 0
elementosDiferentes = [10,'a', False, 12, 15.16]
print(lista)
print(elementosDiferentes)

# Exibindo o primeiro elemento
print(lista[0])
print(elementosDiferentes[0])

# Exibindo o último elemento
print(lista[-1])
print(elementosDiferentes[-1])

# Adicionando um elemento na lista - lista.append()

bycicles = ['trek', 'cannondale', 'redline', 'specialized']
print(bycicles)

bycicles.append('Harley Davidson')
print(bycicles)

# Adicionando em uma posição especifica - lista.insert(x, 'elemento')
bycicles.insert(1, 'ducati')
print(bycicles)

# Para remover um determinado item da lista, use o comando del
del bycicles[1]
print(bycicles)

# O metodo remove() apaga apenas a primeira ocorrência do valor que você especificar.

bycicles.remove('redline')
print(bycicles)

# o metodo count conta a ocorrencia do valor - lista.count('x')

numeros = [1, 5, 1, 4, 1, 7, 7, 15]

qtd1 = numeros.count(1)
qtd7 = numeros.count(7)
print(qtd1)
print(qtd7)

# o metodo pop remove o ultimo caracter e retorna

print(numeros)

ultimo = numeros.pop()

print(numeros)
print(ultimo)

# você pode remover uma posicao especifica com o pop

removerTerceiro = numeros.pop(2)
print(numeros)
print(removerTerceiro)

# len mostra o tamanho da lista, string sao uma lista de caracteres - len(lista)

print(len(numeros))
print(len('Ola'))

# sort ordena sua lista em ordena e altera em ordem crescente ou alfabetica (tabela asc) - lista.sort()
numeros2 = [1, 5, 1, 4, 1, 7, 7, 15]
numeros2.sort()

print(numeros2)

# sorted ordena a lista mas não altera ela sorted(lista)
print(sorted(numeros))
print(numeros)

print(sorted('oláaa'))

# sort pode ser invertido se usar o paramtero lista.sort(Reverse=true)
numeros.sort(reverse=True)
print(numeros)

# ou usar direto o metodo reverse

numeros.reverse()
print(numeros)

# Algumas funções Python são específicas para listas de  números.
# Por exemplo, podemos encontrar facilmente o valor mínimo, o valor máximo e a soma de uma lista de números:

lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(lista2))
print(max(lista2))
print(sum(lista2))

# Copiando uma lista

tracks = [
            'breath', 'on the run', 'time', 'the great gig in the sky', 'money',
            'us and then', 'any colour you like', 'brain damage', 'eclipse'
         ]

copia = tracks
print(copia)

tracks.remove('breath')
tracks.remove('on the run')

print(copia) # lista copiada tambem é afetada, pois ele remove da memória, ou seja o mesmo lugar que cópia estava armazenando

# Printando fatias de lista, o último parametro e o index-1

print(lista2[0:4]) # vai do index 0 até o 3 (4-1)


# Percorrendo a lista com while

i=0
while i < len(lista2):
    print(lista2[i])
    i += 1

# if x in lista, O in verifica se um valor existe dentro de uma lista.

if 5 in lista2:
    print('O número 5 está na lista')

#O Python faz basicamente isso:
valor=5
i = 0
while i < len(lista2):
    if lista2[i] == valor:
        print('O número 5 está na lista')
        break
    i += 1


