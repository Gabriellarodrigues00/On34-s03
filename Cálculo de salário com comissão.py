'''A Artificia, empresa de cosméticos, te contratou para fazer um programa que calcule o salário das 
vendedoras e elas já saibam antes quanto vão ganhar com base nas vendas realizadas.

Como vai funcionar?
O programa deve pedir o valor do salário, o valor em vendas e calcular a comissão conforme a tabela abaixo:

Valor das vendas	Comissão
Até R$ 3.000,00	10%
Até R$ 5.000,00	15%
A partir de R$ 5.000,00	18%
Ao final, você deve mostrar algo como: Este mês você receberá R$ XXX onde XXX é a soma do salário com a comissão.'''

Salario = float(input("Digite seu Salário: "))
vendas = float(input("Digite quanto você vendeu esse mês: "))
comissao1= 3000*10/100
comissao2 = 5000*15/100
comissao3 = 5000*18/100

if vendas <=  3000 :
    print("Este mês você receberá: R$", Salario + comissao1 )
elif vendas <= 5000:
    print("Este mês você receberá: R$", Salario + comissao2 )
else:
    print("Este mês você receberá: R$", Salario + comissao3 )
