# Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no
# # intervalo de 1 até 500.

numerosImpMult = []
for num in range(1, 501):  # de 1 até 500
    if num % 3 == 0:  # multiplos
        if num % 2 == 1:  # Ímpares
            numerosImpMult.append(num)
print((numerosImpMult))
print(f"A soma dos múltiplos é: {sum(numerosImpMult)}.")
      