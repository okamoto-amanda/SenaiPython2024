# #Este é um programa que leia o comprimento de três retas
# #e diz ao usuário se elas podem ou não formar um triângulo.

# Condições Necessárias:
# a + b > c
# a + c > b
# b + c > a
print("Este é um programa que leia o comprimento de três retas e nos diz se elas podem ou não formar um triângulo")
retaA = int(input("Digite o comprimento da primeira reta: "))
retaB = int(input("Digite o comprimento da primeira reta: "))
retaC = int(input("Digite o comprimento da primeira reta: "))

if retaA + retaB >= retaC and retaA + retaC >= retaB and retaB + retaC >= retaA :
    print("É possível formar um triangulo!")