# Em Python, um dicionário é representado entre chaves, {}, com uma série de pares chave-valor entre elas

person = {'name':'Roberto', 'age':37}
print(person['name'])
print(person['age'])

print("")
person['cep']=8142080 # Adicionando novos pares chave-valor dinamicamente
print(person)

print("")
del person['cep'] # Removendo pares chave-valor
print(person)

linguagem_favorita={

    'Roberto':'Python',
    'Felipe': 'java',
    'Arnaldo': 'Assembly',
    'Jose': 'Python'

}

print("")
for nome, linguagem in linguagem_favorita.items(): #Percorrendo um dicionário com um laço
    print(f"Nome: {nome}, Linguagem: {linguagem}")

print("")
for nome in linguagem_favorita.keys(): #Percorrendo todas as chaves de um dicionário com um laço
    print(nome)

print("")
for nome in linguagem_favorita: #Percorrer as chaves, na verdade, é o comportamento-padrão. Colocar .keys() é opicional, pode deixar o código mais legivél mas pode ser omitido.
    print(nome)

print("")
for linguagem in linguagem_favorita.values(): #Percorrendo todas os valores de um dicionário com um laço
    print(linguagem)

print("")
for nome in sorted(linguagem_favorita): #Podemos usar a função sorted() para obter uma cópia ordenada das chaves
    print(nome)

print("")
for linguagem in sorted(linguagem_favorita.values()):
    print(linguagem)

print("")
for linguagem in set(linguagem_favorita.values()): # Para ver cada valor sem repetições, podemos usar um conjunto(set)
    print(linguagem)


print("")
# Às vezes, você vai querer armazenar um conjunto de dicionários em uma lista ou uma lista de itens como um valor em um dicionário. Isso é conhecido como aninhar informações.
enemy_list=[]

for enemy_number in range(5):
    new_enemy={'nome':'inimigo','cor':'vermelho','força':100}
    enemy_list.append(new_enemy)

print("")
for enemy in enemy_list:
    print(enemy)

print("")
# Dicionário de listas

itens={
    'mochila':['comida','agua','jaqueta'],
    'cinto':['arma','faca']
}
print(itens)
print(itens['mochila'])

print("")
# Tuplas são listas imutaveis (valores que não pode mudar)

# A função zip() retorna um objeto zip, que é um iterador de tuplas onde o primeiro item em cada iterador passado é emparelhado e, em seguida, o segundo item em cada iterador passado é emparelhado etc.
# Se os iteradores passados tiverem comprimentos diferentes, o iterador com menos itens decide o comprimento do novo iterador.

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
c = ("Jenny", "Christy", "Louis", "Monica")
x = zip(a, b)
print(list(x))
x = zip(a, c)
print(list(x))

print("")

names = ['John', 'Robert']
surnames = ['Smith', 'De Niro']
numbers = [1, 2]

for name, surname, number in zip(names, surnames, numbers):
    print(name, surname, number)

print("")
for user in zip(names, surnames, numbers):
    print(user)

# Uma tupla se parece exatamente com uma lista, exceto por usar parênteses no lugar de colchetes.
# Depois de definir uma tupla, podemos acessar elementos individuais usando o índice de cada item, como faríamos com uma lista.
print("")

dimensions = (200, 400)
print(dimensions[0])

#Embora não seja possível modificar uma tupla, podemos atribuir um novo valor a uma variável que armazena uma tupla.
#Portanto, se quiséssemos alterar nossas dimensões, poderíamos redefinir a tupla toda:
print("")

dimensions = (400, 500)

print(dimensions)
print(dimensions[0])

# Só é possível utilizar operações de acesso aos elementos de uma tupla.
# Qualquer outra operação que resulte em mudança os elementos não é reconhecida. Exemplos (sort, remove, pop, etc) dimensions = (200, 400, 500, 600)
print("")

print(len(dimensions))
print(dimensions[0:2])
print(max(dimensions))