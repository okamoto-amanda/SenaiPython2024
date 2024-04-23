# Escreva um programa que peça ao usuário para digitar seu
# nome e idade. Em seguida, exiba uma mensagem
# personalizada que inclua o nome e a idade. Lide com o erro
# caso a idade digitada não seja um número.
from time import sleep
try:
    nomeUsuario = input("Por favor digite seu nome: ")
    idadeUsuario = int(input(("Digite sua idade: ")))
    
    sleep(5)
    print(f"Nome de usuário: {nomeUsuario}\nIdade usuario: {idadeUsuario}")
    
        
except ValueError:
    print("Dado inválido")

finally:
    
    print("Fim")