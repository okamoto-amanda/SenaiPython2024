# Faça um programa que leia nome e peso de varias pessoas,
# guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.

# B) Uma listagem com as pessoas mais pesadas.

# C) Um listagem com as pessoas mais leves

nomePessoas = []
pesoPessoas = []
continuacao = 'S'
posicoes = 0
while True:
    nomePessoas.append((input("Digite o nome: ")))
    pesoPessoas.append(float(input('Digite o peso da pessoa cadastrada anteriormente: ')))
    continuacao = input("Deseja continuar? S - SIM N - NÃO: ").upper()
    
    if continuacao ==  'N':
        break
print(nomePessoas+pesoPessoas)

nomePessoas(max(nomePessoas,posicoes))