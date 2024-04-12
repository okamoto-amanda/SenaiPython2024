# Faça um programa que leia nome e peso de varias pessoas,
# guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.

# B) Uma listagem com as pessoas mais pesadas.

# C) Um listagem com as pessoas mais leves

dadosCadastro = []
continuacao = 'S'

while True:
    
    dadosCadastro.append(input("nome: "))
    dadosCadastro.append(int(input("Peso: ")))
    continuacao = input("Deseja continuar? S - SIM N - NÃO: ").upper()
    if continuacao ==  'N':
        break
    
print(dadosCadastro)
criterio = []

for i in dadosCadastro :
    if i is int:
        criterio.append(i)
    else:
        print(i)
    
    
print(sorted(criterio))
print(criterio[0])
        
        
        