#Desafio 1
nome = input("Para começar, digite seu nome completo: ")
#O nome com todas as letras maiúsculas
print(nome.upper())

#O nome com todas as letras minúsculas
print(nome.lower())

#Quantas letras ao todo (sem considerar espaços)
nomeCaracteres = nome.replace(" ","")
print(len(nomeCaracteres))

#Quantas letras tem o primeiro nome
divideNome = nome.split()
print(len(divideNome[0]))
