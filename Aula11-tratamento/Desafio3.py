# Escreva um programa que solicite ao usuário para digitar um
# número inteiro e exiba o resultado da sua raiz quadrada. Lide
# com o erro caso o número seja negativo

try:
    numero = int(input("Por favor, digite um número: "))
    print(f"{numero}² = {numero**2}")

except TypeError:
    prin("Numero inválido")
    