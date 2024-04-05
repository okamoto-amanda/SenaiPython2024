# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou
# no final do jogo.

from random import randint

jogadorPontos = 0

print("Jogo de Par ou Impar")

while True :
    print("\nDigite P para Par e I para Impar")
    escolhaJogador = input("Digite a sua opção: ").upper()
#area do resultado par
    if escolhaJogador == "P":
        numeroJogador = int(input('Digite um valor: '))
        numeroMaquina = randint(0, 10)
        total = numeroJogador + numeroMaquina
        print(f'Você jogou {numeroJogador} e o computador jogou {numeroMaquina}, total: {total}.')
        validacao = total % 2
            
        if validacao == 0:
            print(f" O resultado foi Par. Você venceu!")
            
        else:
            print(f" O resultado foi Impar. Você perdeu!")
            break
#area do resultado impar        
    if escolhaJogador == "I":
        numeroJogador = int(input('Digite um valor: '))
        numeroMaquina = randint(0, 10)
        total = numeroJogador + numeroMaquina
        print(f'Você jogou {numeroJogador} e o computador jogou {numeroMaquina}, total: {total}.')
        validacao = total % 2
            
        if validacao == 1:
            print(f" O resultado foi Impar. Você venceu!")
            
        else:
            print(f" O resultado foi Par. Você perdeu!")
        
            break
    jogadorPontos = jogadorPontos + 1
print(f"O jogo acabou. Você venceu {jogadorPontos} vezes consecutivas")
