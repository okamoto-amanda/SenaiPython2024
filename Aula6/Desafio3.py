# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores

contador = 1
print("Por favor, digite alguns números e o programa vai te dar o maior, o menor e sua média")

maior = 0
menor = 0
continuar = "S"

while continuar != "N":
    numerosUsuario = int(input("Por favor, digite seu palpite: "))
    
    if contador == 1 :
        maior = numerosUsuario
        menor = numerosUsuario
    else: 
        if numerosUsuario > maior:
            maior = numerosUsuario
        if numerosUsuario < menor:
            menor = numerosUsuario
        contador += 1
        
    continuar = str(input("Deseja continuar? ")).upper()
media = numerosUsuario/contador

print(media)
print(maior)
print(menor)

#NAO TERMINOU