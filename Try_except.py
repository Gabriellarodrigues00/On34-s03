print("Vamos rachar a conta")

valortotal1 = float(input("Qual o valor gasto? "))
amigos = int(input("Quantas pessoas? "))

try:
    print("Cada pessoa deve pagar: R$", valortotal1/amigos)

except:
    print("Você não pode colocar 0 para amigos")


try: 
    Nota = float(input("Qual a sua nota?" "(De 0 a 10:) "))
    
    if Nota >= 7 : 
        print("Aprovada")
    else :
        print("Reprovada")

except:
    print("Você precisa digitar um número entre 0 e 10")

