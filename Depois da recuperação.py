'''Agora precisamos checar se quem ficou de recuperação tirou nota suficiente para passar. A regra continua a mesma: A nota mínima de aprovação é 7. Se a aluna tirou ao menos 5, ela fica de recuperação, e abaixo de 5, ela está reprovada. 
Na recuperação, a nota mínima de aprovação é 8.'''

nota = float(input("Qual a nota" "(De 0 a 10):"))


if nota >=7 : 
    print("Aprovada")
elif nota >=5 :
    print("Recuperação")
    nota_recuperacao = float(input("Qual sua nota da recuperação?" "(De 0 a 10):"))
    if nota_recuperacao >=8 :
        print("Aprovada na recuperação")
    else :
        print("Reprovada na recuperação")
else:
    print("Reprovada")



