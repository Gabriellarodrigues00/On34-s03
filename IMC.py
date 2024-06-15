'''Você já conheceu o cálculo do IMC e agora precisa montar um programa que peça o nome da pessoa, o peso em quilos e a altura em metros. 
Será necessário mostrar o resultado com base na tabela da OMS (Organização Mundial de Saúde):

IMC	Classificação
Abaixo de 18,5	Magreza
Entre 18,5 e 24,9	Normal
Entre 25,0 e 29,9	Sobrepeso
Entre 30,0 e 39,9	Obesidade
Maior que 40,0	Obesidade grave

Dependendo do valor do IMC, o programa precisa responder qual a classificação da pessoa. '''

Nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso/altura**2



if IMC < 18.5:
    print("Olá", Nome, "Sua classificação é de Magreza")
elif 18.5 <= IMC <= 24.9 :
    print("Olá", Nome, "Sua classificação é de Normal")
elif 25.0 <= IMC <= 29.9 :
    print("Olá", Nome, "Sua classificação é de Sobrepeso")
elif 30.0 <= IMC <= 39.9:
    print("Olá", Nome, "Sua classificação é de Obesidade")
else:
    print("Olá", Nome, "Sua classificação é de Obesidade grave")






