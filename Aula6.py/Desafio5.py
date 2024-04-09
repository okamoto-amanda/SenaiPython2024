# Crie um programa que leia a idade e o sexo de varias
# pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:

# A) Quantas pessoas tem mais de 18 anos.

# B) Quantos homens foram cadastrados.

# C) Quantas mulheres tem menos de 20 anos.

print("Este é um programa que armazena alguns dados")

maioridade = 0
homens = 0
mulheresMaiores20 = 0

while True:

        idade = int(input("Por favor digite a idade da pessoa cadastrada: "))
        sexo = input("Por favor digite o sexo da pessoa cadastrada: ").upper()
        continuacao = input("Se deseja continuar digite S - Sim: ").upper()
        
        if idade >= 18: 
            maioridade +=1
            
        if idade >= 20 and sexo == "F":
            mulheresMaiores20 += 1
            
        if sexo == "M":
            homens += 1
            
        if continuacao != "S":
            break
        
print(f"Pessoas maiores de idade: {maioridade}, Quantidade de homens: {homens}. Quantidade de mulheres maiores de 20: {mulheresMaiores20}")
    