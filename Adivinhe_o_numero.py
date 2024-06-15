'''Neste programa, você precisa definir um número entre 1 e 100 e pedir para o usuário tentar acertar. 
Você vai dizer se a pessoa acertou, chutou muito alto ou chutou muito baixo. Diga qual o numero'''

#import random
#numero_secreto1 = random.randint(1,100)
#acertou = False  outra for de fazer sendo um numero aleatório 

numero_secreto = 10

print("Seja bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que eu estou pensando")


numero_escolhido = int(input("Escolha seu número de 0 a 100: "))

if numero_escolhido == numero_secreto :
    print("Você acertou!")

elif numero_escolhido < numero_secreto :
    print("Seu palpite foi muito baixo.Tente novamente")

else:
    print("Seu palpite foi muito alto.Tente novamente")

print("O número escolhido era: ", numero_secreto)

