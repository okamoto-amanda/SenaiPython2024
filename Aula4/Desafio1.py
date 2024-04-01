# Escreva um programa para aprovar um empréstimo bancário
# para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai
# pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

print("Este é um programa que calcula financiamentos bancários")
casa = int(input("Por favor, digite o valor total do imóvel: "))
salario = float(input("Por favor, digite o valor do salário bruto: "))
tempo = int(input("Digite em quantos anos pretende financiar: "))
margem = salario*0.3
meses =  tempo * 12
prestacao = casa / meses

#print(casa , salario, tempo, margem, meses)
if prestacao > margem :
    print(f" Sua margem é de {margem}. Reprovado")
else :
    print(f" Sua margem é de {margem} \nSua prestação será de {meses} fixas de R${round(prestacao,2)} por mês, durante {tempo} anos")