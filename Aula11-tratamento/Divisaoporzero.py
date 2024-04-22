#Divisao por zero

try:
    divisao = 5 / 0 
    print(divisao)
except ZeroDivisionError:
    print("Não existe divisão por ZERO!")