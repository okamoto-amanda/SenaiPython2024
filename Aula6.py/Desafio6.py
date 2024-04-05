# Crie um programa que leia o nome e o preço de vários
# produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:

# A) Qual é o total gasto na compra.

# B) Quantos produtos custam mais de R$ 100,00.

# C) Qual é o nome do produto mais barato.

print("Cesta de compras")
produto100 = 0

while True:
    
    input("Digite o nome do item: ")
    itemValor = int(input("Digite o valor do item: "))
    
    totalGasto = totalGasto + itemValor
    
    
    if itemValor >= 100 :
        produto100 += 1
        
    
    


