# A confederação Nacional de Natação precisa de uma programa
# que leia o ano de nascimento de uma atleta e mostre sua
# categoria, de acordo com a idade.

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 24 anos: SÊNIOR
# Acima: MASTER

print("Este é um programa que categoriza os atletas de acordo com sua idade")
nascimentoAtleta = int(input("Por favor, digite o ano de nascimento para que o atleta possa ser categorizado: "))
idade = 2024 - nascimentoAtleta
print(idade)

if idade < 10 :
    print("Atleta categoria MIRIM")
elif idade < 15 :
    print("Atleta categoria INFANTIL")
elif idade < 20 :
    print("Atleta categoria JUNIOR")
elif idade < 25 :
    print("Atleta categoria JUNIOR")
else :
    print("Atleta categoria MASTER")
