# Crie um programa que vai ler vários números e colocar em
# uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores impares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

from random import randint
listaCompleta = []
listaPares = []
listaImpares = []

while len(listaCompleta) < 10:
    listaCompleta.append(randint(0, 30))
    
for i in listaCompleta:
    if i % 2 == 0:
            listaPares.append(i)
    else: 
            listaImpares.append(i)        
            
print(f'Lista completa:{listaCompleta}')
print(f'Somente numeros pares:{listaPares}')
print(f'Somente numeros impares:{listaImpares}')