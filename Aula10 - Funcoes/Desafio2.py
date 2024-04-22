# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.
# Ex:
# escreva(‘Olá, mundo!!’)
# Saída
# -----------------------------------
#  Olá, mundo
# -----------------------------------

textoUsuario = input("Digite seu texto: ")

def escreva(textoUsuario):
    print(f"-" * (len(textoUsuario)) +"\n"+ textoUsuario + "\n"+"-" *(len(textoUsuario)))
    
escreva(textoUsuario)