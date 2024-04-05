# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores


numerosUsuario = []
print("Por favor, digite alguns números e o programa vai te dar o maior, o menor e sua média")
respostaUsuario = 'SIM'

while respostaUsuario == 'SIM':
    valorUsuario = int(input("Digite um valor: "))
    numerosUsuario.append(valorUsuario)
    respostaUsuario = (input("Se quiser continuar, digite SIM ")).upper()
else:
    numerosUsuario = sorted(numerosUsuario)
    print(f"A soma entre eles é {sum(numerosUsuario)}. O maior é {max(numerosUsuario)}, e o menor é o {min(numerosUsuario)}")
