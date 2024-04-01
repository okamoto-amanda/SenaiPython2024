#Faça um programa que leia uma frase pelo teclado e mostre
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

fraseUsuário = input("Este é um programa que faz análise de uma frase \nPor favor, digite uma frase completa: ")
fraseContagem = fraseUsuário.count("a")
frasePrimeiraLetra = fraseUsuário.find("a")
fraseUltimaLetra = fraseUsuário.rfind("a")

print(f"A letra a apareceu {fraseContagem} vezes")
print(f"A letra a apareceu na {frasePrimeiraLetra + 1} posição")
print(f"A letra a apareceu na {fraseUltimaLetra + 1} posição")