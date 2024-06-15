'''Você já deve ter ligado em uma empresa e ouvido uma lista de opções com números que deviam ser digitados com a opção escolhida para ser direcionada a um certo departamento. 
Seu trabalho agora é criar um minissistema de telemarketing.'''

print("Olá! Obrigada por ligar para nós!") 
print("Para falar com Financeiro, digite 1.") 
print("Para falar com Administrativo, digite 2.")
print("Para falar com Recursos Humanos, digite 3") 
print("Para falar com Assistência Técnica, digite 4")
resposta = int(input("Digite o setor escolhido: "))


if resposta == 1 :
    departamento = "Financeiro"
    print("Você será direcionada para o Financeiro.")
    
elif resposta == 2 :
    departamento = "Administrativo"
    print("Você será direcionada para o Administrativo.")

elif resposta == 3 :
    departamento = "Recursos Humanos"
    print("Você será direcionada para os Recursos Humanos")

elif resposta == 4 :
    departamento = "Assistência Técnica"
    print("Você será direcionado para a Assistência Técnica") 

else : 
    print("Opção inválida.Por favor, tente novamente!")


print("Você pode deixar recado para ", departamento, "ou falar com um atendente?")
print("Para deixar recado, digite 1")
print("Para falar com atendente, digite 2")

escolha = int(input("Digite o número da opção desejada: "))

if escolha == 1:
    print("Você pode deixar seu recado agora:")

elif escolha == 2:
    print("Por favor, aguarde seu atendimento")

else :
    print("Opção inválida.Por favor, tente novamente")