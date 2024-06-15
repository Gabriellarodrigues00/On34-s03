'''Fazer prova é sempre uma pressão, então a professora resolveu que as alunas poderiam ser aprovadas de outra forma: 
ou ter ao menos 7 na nota ou 75% de presença.'''

Nota = float(input("Qual a sua nota?" "(De 0 a 10:) "))
Presença = float(input("Qual a sua presença?" "(De 0 a 100:) "))


if Nota >= 7 or Presença >= 75 :
    print("Aprovada")

else :
    print("Reprovada")