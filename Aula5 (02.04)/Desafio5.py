# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar desconsidere-o.

numerosRecebidos = []
for i in range(6):
    numeroUsuario = int(input(f"Digite o {i+1}º numero: "))
    if numeroUsuario % 2 == 0:
        numerosRecebidos.append(numeroUsuario)

print(f"A soma dos números é {sum(numerosRecebidos)}")