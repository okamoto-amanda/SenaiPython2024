# Crie um programa que leia o nome e o preço de vários
# produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:

# A) Qual é o total gasto na compra.

# B) Quantos produtos custam mais de R$ 100,00.

# C) Qual é o nome do produto mais barato.

print("Cesta de compras")
produto100 = 0
totalGasto = 0
produtoMaisCaro = 0
produtoBarato = 10000
cestaDeCompras = []
Stop = 'PARE'


while True:
    respostaUsuario = input("Digite o nome do item: ").upper()
    cestaDeCompras.append(respostaUsuario)
    itemValor = int(input("Digite o valor do item: "))
    totalGasto = totalGasto + itemValor
    
    continuar = input("Se deseja continuar digite S (Sim): ").upper()
    
    
    if itemValor >= 100:
        produto100 += 1
    
    if itemValor >= produtoMaisCaro:
        produtoMaisCaro = itemValor
    
    if itemValor <= produtoBarato:
        produtoBarato = itemValor
    
    if continuar != 'S':
        break
    

print(f'\nItens da sua Cesta de Compras{cestaDeCompras}')
print(f'Total gasto:{totalGasto}')
print(f'Quantidade de produtos que custam mais que R$100:{produto100}')
print(f'Produto mais caro custou R${produtoMaisCaro}')
print(f'O produto mais barato custou R${produtoBarato}')    

    
#NAO TERMINOU
