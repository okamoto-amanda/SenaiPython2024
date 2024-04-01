# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:

# Equilátero: Todos os lados iguais

# Isósceles: Dois lados iguais

# Escaleno: Todos os lados diferentes

print("Este é um programa que leia o comprimento de três retas e nos diz se elas podem ou não formar um triângulo")
retaA = int(input("Digite o comprimento da primeira reta: "))
retaB = int(input("Digite o comprimento da primeira reta: "))
retaC = int(input("Digite o comprimento da primeira reta: "))

if retaA + retaB >= retaC and retaA + retaC >= retaB and retaB + retaC >= retaA :
    print("É possível formar um triangulo!")
    if retaA == retaB and retaA == retaC :
        print("Triângulo tipo Equilátero!")
    elif retaA == retaB or retaB == retaC :
        print("Triângulo tipo Isósceles!")
    else:
        print("Triângulo tipo Escaleno!")
else :
    print("Não é possível formar um triângulo")