# Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

termo = int(input("Por favor, digite o primeiro termo da Progressão: "))
razao = int(input("Por favor, digite a razão: "))
for i in range(10):
    termo + (i+1) * razao
    
print(i)