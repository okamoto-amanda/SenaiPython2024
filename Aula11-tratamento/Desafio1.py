# Escreva um programa que peça ao usuário para digitar dois
# números e divida o primeiro número pelo segundo. Certifique-se
# de lidar com a possibilidade de divisão por zero.
while True:
    try:
        print("Este é um programa que faz calculos com os números atribuidos pelo usuario")
        a = int(input("Digite o primeiro valor: "))
        b = int(input("Digite o segundo valor: "))

    except ZeroDivisionError:
        print("Não existe divisão por zero!\n")
    
    except ValueError:
        print("Você digitou algum valor divergente!\n")
    
    else:
        print(f"A divisão desses dois números é {a/b}")
        break