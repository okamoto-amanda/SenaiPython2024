# Faça um programa que tenha uma função chamada maior(), que
# receba três parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é
# o maior.

a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))
    
def maior(a, b, c):
    valores = [a,b,c]
    print(f"O maior número é o {max(valores)}")

maior(a,b,c)