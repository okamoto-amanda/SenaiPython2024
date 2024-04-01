# Crie um programa que leia duas notas entre 0 a 10 de um aluno
# e calcule sua média, mostrando uma mensagem no final, de
# acordo com a média atingida.
# Média abaixo de 5.0: REPROVADO

# Média entre 5.0 a 6.9: RECUPERAÇÃO

# Média igual ou superior a 7.0: APROVADO

print("Este é um programa que calcula a média atingida de um aluno")
notaA = int(input("Por favor, digite a primeira nota. Serão aceitos valores de 0 a 10: "))
notaB = int(input("Por favor, digite a segunda nota. Serão aceitos valores de 0 a 10: "))

media = (notaA + notaB) / 2
print(media)

if media < 5.0 :
    print("Aluno Reprovado!")
elif media > 5.0 and media < 6.0 :
    print("Aluno em Recuperação!")
else :
    print("Aluno Aprovado!")
