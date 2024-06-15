'''Faça um programa que peça para a pessoa entrar com a nota de 0 a 10 e a porcentagem de presença nas aulas. 
Imprima se a aluna foi aprovada ou reprovada. A nota mínima de aprovação é 7 e a de presença é 75%.'''

Nota = float(input("Qual a sua nota?" "(De 0 a 10:) "))
Presença = float(input("Qual a sua presença?" "(De 0 a 100:) "))


if Nota >= 7 and Presença >= 75 :
    print("Aprovada")

else :
    print("Reprovada")


