# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em
# forma tabular

itens = ('Arroz',26, 'Feijão',8, 'Macarrão',3, 'Banana',40)
print(itens)
print(len(itens))

for i in range (0, len(itens)):
    if type(itens[i]) is str:
        print(f"Produto: {itens[i]}....Preço: R${itens[i+1]},00")
        
#print(type(itens))