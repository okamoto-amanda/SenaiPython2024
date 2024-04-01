frase = "Curso de Python"
nome = "Amanda Okamoto"

#Analisar o tamanho da frase
print(len(frase))
print(len(nome))

#Conta quantas vezes um caractere específico aparece 
print(frase.count("o"))

#Indica onde em qual posição se inicia uma frase
print(frase.find("Python"))
print(nome.find("Okamoto"))

#Indica se uma palavra existe ou não na string
print("Python" in frase)
print("Santos" in nome)
print("Silva" in nome)
print("Oliveira" in nome)
print("Siqueira" in nome)
print("Ribeiro" in nome)
