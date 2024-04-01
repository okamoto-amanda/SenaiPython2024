# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.



print("Este é um programa que calcula o preço de uma passagem baseada nos quilômetros da viagem desejada")
distanciaUsuario = int(input("Por favor, digite a distância do seu percurso: "))

if distanciaUsuario >= 200:
    tarifaCheia = distanciaUsuario * 0.50
    print (f"Você digitou {distanciaUsuario}. O valor cobrado pela viagem é de R${tarifaCheia}")
    
else :
    tarifaReduzida = distanciaUsuario * 0.45
    print (f"Você digitou {distanciaUsuario}. O valor cobrado pela viagem é de R${tarifaReduzida}")