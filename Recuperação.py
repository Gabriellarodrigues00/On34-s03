'''Agora temos três condições! Faça um programa que peça para a pessoa entrar com a nota de 0 a 10 e imprima se a aluna foi aprovada reprovada ou está em recuperação. A nota mínima de aprovação é 7. 
Se a aluna tirou ao menos 5, ela fica de recuperação, mas abaixo de 5, ela está reprovada.'''

Nota = float(input("Qual a sua nota?" "(De 0 a 10: )"))


if Nota >=7 :
	print("Aprovada")
elif Nota >=5 : 
	print("recuperação")
else :
    print("Reprovada")
