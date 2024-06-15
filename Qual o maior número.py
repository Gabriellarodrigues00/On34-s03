'''Faça um programa que peça dois números inteiros de 0 a 100 e imprima o maior.

A saída deve ser parecida com isso: O maior número é X sendo que X deve ser o maior número dado pelo usuário.

Bônus1: tente fazer como função.

Bônus2: peça para o usuário 3 números e diga o mais alto.'''


num1 = int(input("Digite o primeiro número (0 a 100): "))
num2 = int(input("Digite o segundo número (0 a 100): "))

if num1 > num2:
    print("O maior número é", num1)
else:
    print("O maior número é", num2)


def encontrar_maior(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
def dois():
    num1 = int(input("Digite o primeiro número (0 a 100): "))
    num2 = int(input("Digite o segundo número (0 a 100): "))
maior = encontrar_maior(num1, num2)
print("O maior número é" , maior)

dois()


def encontrar_maior_de_tres(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def tres():
    num1 = int(input("Digite o primeiro número (0 a 100): "))
    num2 = int(input("Digite o segundo número (0 a 100): "))
    num3 = int(input("Digite o terceiro número (0 a 100): "))
    maior = encontrar_maior_de_tres(num1, num2, num3)
    print("O maior número é", maior)
tres()