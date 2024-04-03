
''' Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''

numeroUsuario = int(input("Por favor, digite um número que te mostrarei sua tabuada: "))
for i in range(1,11,1):
    print(f"{i} x {numeroUsuario} = {i*numeroUsuario}")