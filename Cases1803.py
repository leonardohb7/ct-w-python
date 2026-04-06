#Operador Ternário
x=4
resultado = "Par" if x % 2 == 0 else "Impar"
print(resultado)

option = 'a'


# Match Case
match option:
    case 'a':
        print("Opção A selecionada")
    case 'b':
        print("Opção B selecionada")
    case _:
        print("Opção Invalida")

n=0

match n:
    case 0:
        print("Zero")
    case 1|2|3:
        print("Pequeno")
    case _:
        print("Grande")
