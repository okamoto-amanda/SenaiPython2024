# Escreva um programa que peça ao usuário para digitar dois
# números e divida o primeiro número pelo segundo. Certifique-se
# de lidar com a possibilidade de divisão por zero.

try:
    print("Este é um programa que faz calculos com os números atribuidos pelo usuario")
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    print(f"A divisão desses dois números é {a/b}")
    
except ZeroDivisionError or TypeError:
    print("Você digitou algum valor divergente")
finally:
    print("Fim")