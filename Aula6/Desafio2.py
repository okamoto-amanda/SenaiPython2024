# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o 999).
parada = 999
tentativa = int(input("Este programa tem uma condição de parada, por favor, digite seu palpite: "))
i = 1

while tentativa != parada:
    tentativa += tentativa
    i += 1
    
else: 
    print("Parabéns!")
    print(f"Você adivinhou em {i} tentativas. A soma de suas tentativas foi {tentativa}")
    