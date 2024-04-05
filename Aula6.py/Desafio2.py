# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o 999).

tentativa = int(input("Este programa tem uma condição de parada, por favor, digite seu palpite: "))
tentativaLista = []
parada = 999
soma = 0

while tentativa != parada:
    tentativaLista.append(tentativa)
    tentativa = int(input("Digite um novo seu palpite: "))
    
else: 
    print("Parabéns!")
    print(len(tentativaLista))
    print(f"Você adivinhou em {len(tentativaLista)} tentativas. A soma de suas tentativas foi {sum(tentativaLista)}")
    