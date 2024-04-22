# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.
# Ex:
# escreva(‘Olá, mundo!!’)
# Saída
# -----------------------------------
#  Olá, mundo
# -----------------------------------


def escreva():
    textoUsuario = input("Digite seu texto: ")

    print(f"-" * 10 +"\n"+ textoUsuario + "\n"+"-" *10)
    
escreva()