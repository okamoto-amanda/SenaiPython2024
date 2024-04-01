
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares ela pode comprar.
#Considere o dólar = R$ 5,00 

print("Este programa te diz quantos dólares você pode comprar atualmente.\nConsideramos o dólar à cotação de R$ 5,00")
valorReais = float(input("(Serão aceitos valores inteiros como 10, 20, 30.\nSerão aceitos valores em reais e centavos, separados por ponto. Ex: 5.10. 7.15, 8.20... Por favor digite o quanto você possui em Reais: "))
arredondarReais = round(valorReais, 2)
dolar = 5
converterDolar = arredondarReais /dolar
print(f"Você digitou R${arredondarReais} \n Você pode comprar até U${converterDolar:.2f}")
