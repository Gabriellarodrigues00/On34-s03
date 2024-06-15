'''O Departamento de Trânsito da sua cidade te contratou para fazer um programa que diga se o carro passou dentro da
 velocidade permitida ou acima da velocidade. 
Se ele passar acima da velocidade máxima permitida, calcule a multa. 
Para até 20% acima da velocidade máxima permitida, o valor é de R$ 200 e, acima disso, o valor é de R$ 350.
Além da velocidade do veículo, você deve solicitar a velocidade máxima da via.

Bônus: faça o programa com função (def) para facilitar, já que o Departamento de Trânsito precisará calcular a
 velocidade de todos os carros que estão passando naquela via (e serão muitos!).'''

print("Calcule a multa: ")

'''velocidade_veiculo = float(input("Qual a velocidade do veículo? "))
velocidade_max_via = int(input("Qual a velocidade máxima da via? "))

if velocidade_veiculo > velocidade_max_via :
    print("Velocidade máxima ultrapasada")
    if velocidade_veiculo  <= velocidade_max_via + velocidade_max_via* (20/100) :
        print("Multa no valor de R$200,00")
    else:
        print("Multa no valor de R$350,00")
else:
    print("Velocidade não ultrapassada")
    print("Multa no valor de R$0,00")'''


def calcular_multa(velocidade_veiculo, velocidade_maxima):
    excesso = velocidade_veiculo - velocidade_maxima
    percentual_excesso = (excesso / velocidade_maxima) * 100
    
    if percentual_excesso > 20:
        multa = 350
    elif percentual_excesso > 0:
        multa = 200
    else:
        multa = 0
        
    return multa

def verificar_velocidade():
    velocidade_veiculo = float(input("Digite a velocidade do veículo (em km/h): "))
    velocidade_maxima = float(input("Digite a velocidade máxima da via (em km/h): "))
    
    if velocidade_veiculo <= velocidade_maxima:
        print("O veículo está dentro do limite de velocidade.")
    else:
        multa = calcular_multa(velocidade_veiculo, velocidade_maxima)
        if multa == 200:
            print("O veículo está acima da velocidade máxima permitida. Multa de R$ 200.")
        elif multa == 350:
            print("O veículo está muito acima da velocidade máxima permitida. Multa de R$ 350.")


verificar_velocidade()


