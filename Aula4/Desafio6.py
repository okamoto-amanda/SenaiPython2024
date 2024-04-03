
# Crie um programa que faça o computador jogar Jokenpô com você:

from random import choice

print("Vamos jogar Jokenpo!")

variavelMaquina = ("PEDRA", "PAPEL", "TESOURA")
variavelUsuario = (input("Escolha Pedra, Papel ou Tesoura: "))

escolhaMaquina = choice(variavelMaquina)
escolhaUsuario = variavelUsuario.upper()

if escolhaUsuario in variavelMaquina :
    print(f"A Máquina escolheu: {escolhaMaquina}")
    print(f"Você escolheu: {escolhaUsuario}")
