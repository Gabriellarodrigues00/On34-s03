'''Faça um programa que peça a temperatura atual em graus Celsius e imprima como está o dia, 
conforme a tabela abaixo:

Temperatura	Classificação
Acima de 27 graus	dia quente
De 20 a 27 graus	dia agradável
Abaixo de 20 graus	dia frio
Bônus: você pode começar perguntando se a entrada será em Celsius ou Fahrenheit 
e, se for em Fahrenheit, transformar em Celsius. O cálculo é (°F − 32) × 1,8 = °C.'''


qual_a_medida = input("Como está a temperatura? celsius ou fahrenheit: ")
temperatura = float(input("Qual a temperatura ?"))
conversao = (temperatura-32)*5/9


if qual_a_medida == 'fahrenheit' : 
    if conversao > 27 :
        print("Dia quente")
    elif 20 <= conversao <= 27 :
        print("Dia agradável")
    else:
        print("Dia frio")

else :
    if temperatura > 27 :
        print("Dia quente")
    elif 20 <= temperatura <= 27 :
        print("Dia agradável")
    else:
        print("Dia frio")
    



    