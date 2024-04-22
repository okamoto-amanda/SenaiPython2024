# Faça um programa que tenha uma função chamada contador(), que
# receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função
# criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada


def contador(inicio, fim, passo):
    for i in range(inicio, (fim+1), passo): #fim+1 para que o valor 10 apareca entre os numeros
            print(i)
    print("\n")
            
contador(1,10,1)

contador(10,0,-2)

a = int(input('Digite o valor inicial: '))
b = int(input('Digite o valor final: '))
c = int(input('Digite os passos: '))