#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nomeUsuario = input("Por favor, digite seu nome completo: ")
nomeCompleto = nomeUsuario.replace(" ","")
nomeVerificação = nomeCompleto.count("Silva")
print(nomeVerificação)
