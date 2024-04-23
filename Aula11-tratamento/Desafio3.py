# Escreva um programa que solicite ao usuário para digitar um
# número inteiro e exiba o resultado da sua raiz quadrada. Lide
# com o erro caso o número seja negativo
from math import sqrt

while True:
    try:
        numero = int(input("Por favor, digite um número: "))
        numero2 = sqrt(numero)

    except:
        print("Numero inválido. Tente novamente.\n")

    else:
        print(f"A raiz quadrada de {numero} é {numero2}") 
    break
    