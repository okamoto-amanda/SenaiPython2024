#Jokenpo

from random import choice

variaveis = {0:"Pedra", 1:"Papel", 2:"Tesoura"}
valor = 0
valorFicha = 2
acertou = False

while acertou == False:
        
    jogadaComputador = choice(1)
    
    jogador = int(input("Entre com um número para jogar: 0 - Pedra | 1 - Papel | 2 - Tesoura: "))
        
    if variaveis[jogadaComputador] == "Pedra" and variaveis[jogador] == "Papel":
            print("_____________________________________________________________________________________________")
            print(f"Você ganhou! - Computador: {variaveis[jogadaComputador]} e Jogador: {variaveis[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True
    elif variaveis[jogadaComputador] == "Papel" and variaveis[jogador] == "Pedra":
            print("_____________________________________________________________________________________________")
            print(f"Você perdeu! - Computador: {variaveis[jogadaComputador]} e Jogador: {variaveis[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True 
    elif variaveis[jogadaComputador] == "Pedra" and variaveis[jogador] == "Tesoura":
            print("_____________________________________________________________________________________________")
            print(f"Você perdeu! - Computador: {variaveis[jogadaComputador]} e Jogador: {variaveis[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True 
    elif variaveis[jogadaComputador] == "Tesoura" and variaveis[jogador] == "Pedra":
            print("_____________________________________________________________________________________________")
            print(f"Você ganhou! - Computador: {variaveis[jogadaComputador]} e Jogador: {variaveis[jogador]}")        
            print("_____________________________________________________________________________________________")
            acertou = True        
    elif variaveis[jogadaComputador] == "Tesoura" and variaveis[jogador] == "Papel":
            print("_____________________________________________________________________________________________")
            print(f"Você perdeu! - Computador: {variaveis[jogadaComputador]} e Jogador: {variaveis[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True
    elif variaveis[jogadaComputador] == "Papel" and variaveis[jogador] == "Tesoura":
            print("_____________________________________________________________________________________________")
            print(f"Você ganhou! - Computador: {variaveis[jogadaComputador]} e Jogador: {variaveis[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True   
    elif variaveis[jogadaComputador] == "Pedra" and variaveis[jogador] == "Tesoura":
            print("_____________________________________________________________________________________________")
            print(f"Você perdeu! - Computador: {variaveis[jogadaComputador]} e Jogador: {variaveis[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True
    elif variaveis[jogadaComputador] == "Tesoura" and variaveis[jogador] == "Pedra":
            print("_____________________________________________________________________________________________")
            print(f"Você ganhou! - Computador: {variaveis[jogadaComputador]} e Jogador: {variaveis[jogador]}")
            print("_____________________________________________________________________________________________")
            acertou = True
    elif variaveis[jogadaComputador] == variaveis[jogador]:
            print("_____________________________________________________________________________________________")
            print(f"Empate! - Computador: {variaveis[jogadaComputador]} e Jogador: {variaveis[jogador]}")
            print("_____________________________________________________________________________________________")
                  
    else:
        print("Entre com valores válidos")
        continue
    valor = valor + valorFicha