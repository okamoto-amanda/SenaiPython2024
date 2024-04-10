from random import randint
numerosAleatorios = []

while len(numerosAleatorios) < 5:
    numerosAleatorios.append(randint(0, 50))
    
tuplaNumeros = tuple(numerosAleatorios)
print(numerosAleatorios)

print(f'O maior numero sorteado foi: {max(tuplaNumeros)}')
print(f'O menor numero sorteado foi: {min(tuplaNumeros)}')

