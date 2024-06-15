'''Precisamos checar a nota do 1º bimestre e do 2º bimestre e fazer a média. Se a pessoa ficou de recuperação, é necessário checar se tirou nota suficiente para passar. A regra é: A nota mínima de aprovação é 6. 
Se a aluna tirou ao menos que 6, ela fica de recuperação, e abaixo de 3, ela está reprovada.
 Na recuperação, a nota mínima de aprovação é 7.
Faça um programa que peça para a pessoa entrar com as duas notas de 0 a 10 e
 imprima se a aluna foi aprovada, reprovada ou está em recuperação. 
 Se estiver em recuperação, peça para entrar com a nota da recuperação e imprima se foi aprovada ou reprovada.'''

nota1 = float(input("Qual a sua nota do 1º bimestre" "(De 0 a 10):"))
nota2 = float(input("Qual a sua nota do 2º bimestre" "(De 0 a 10):"))
media = (nota1+nota2)/2

if media >=6 : 
    print("Aprovada")
elif media >= 3 :
    print("Recuperação")
    nota_recuperacao = float(input("Qual sua nota da recuperação?" "(De 0 a 10):"))
    if nota_recuperacao >=7 :
        print("Aprovada na recuperação")
    else :
        print("Reprovada na recuperação")
else:
    print("Reprovada")
