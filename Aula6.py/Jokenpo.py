from random import choice

#lista de opções do jokenpo
variaveis = ["PEDRA" , "PAPEL"  , "TESOURA"]

escolhaMaquina = choice(variaveis)
escolhaJogador= input("Informe sua escolha no jokenpo : ").upper()

if escolhaMaquina == escolhaJogador :
    print(f"Jogador escolheu {escolhaJogador}\nMaquina escolheu {escolhaMaquina}\nEmpate !! ")
    
elif  escolhaMaquina == "PEDRA" and escolhaJogador == "TESOURA":
    print(f"Jogador escolheu {escolhaJogador}\nMaquina escolheu {escolhaMaquina}\nVocê perdeu !! ")
    
elif escolhaMaquina == "PEDRA" and escolhaJogador == "PAPEL" :
    print(f"Jogador escolheu {escolhaJogador}\nMaquina escolheu {escolhaMaquina}\nVocê venceu !! ")

elif escolhaMaquina == "TESOURA" and escolhaJogador == "PAPEL" :
    print(f"Jogador escolheu {escolhaJogador}\nMaquina escolheu {escolhaMaquina}\nVocê perdeu !! ")
    
elif escolhaMaquina == "TESOURA" and escolhaJogador == "PEDRA" :
    print(f"Jogador escolheu {escolhaJogador}\nMaquina escolheu {escolhaMaquina}\nVocê venceu !! ")

elif escolhaMaquina == "PAPEL" and escolhaJogador == "TESOURA" :
    print(f"Jogador escolheu {escolhaJogador}\nMaquina escolheu {escolhaMaquina}\nVocê venceu !! ")

elif escolhaMaquina == "PAPEL" and escolhaJogador == "PEDRA" :
    print(f"Jogador escolheu {escolhaJogador}\nMaquina escolheu {escolhaMaquina}\nVocê venceu !! ")