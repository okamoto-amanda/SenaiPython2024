from random import randint

numerosAleatorios = []

while len(numerosAleatorios) < 5:
    numerosAleatorios.append(randint(0, 50))
    
tuplaNumeros = tuple(numerosAleatorios)
print(numerosAleatorios)

print(min(tuplaNumeros))
print(max(tuplaNumeros))

