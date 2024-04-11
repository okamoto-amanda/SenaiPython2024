# Crie um programa que cria uma matriz de dimensão 3x3 e
# preencha com valores lidos pelo teclado.
# No final mostre a Matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
c = 0

for i in range(0,3):
    for j in matriz[i]:
        
        if c == 3:
            c = 0
        
        numero = int(input(f"Digite um valor para a posição {i},{c}: "))
        matriz[i][c] = numero
            
        c += 1
print(matriz)       
for i in range(0,3):
    print(matriz[i])
    i += 1

