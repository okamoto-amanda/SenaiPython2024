# Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e as
# suas respectivas posições na lista.

Lista1 = []
while len(Lista1) < 5:
    Lista1.append(int(input("Por favor digite um número: ")))
    
print(sorted(Lista1))
print(f'O mair valor da lista é {max(Lista1)}. Sua posição é a {Lista1.index(max(Lista1))+1}ª posição')
print(f'O menor valor da lista é {min(Lista1)}. Sua posição é a {Lista1.index(min(Lista1))+1}ª posição ')