
numerosUsuario = []
numerosPares = []

while len(numerosUsuario) < 4:
    numerosUsuario.append(int(input("Por favor digite um número: ")))

tuplaNumeroUsuario = tuple(numerosUsuario)                   
print(numerosUsuario)

# Quantas vezes apareceu o valor 9.
print(f'O numero 9 apareceu {tuplaNumeroUsuario.count(9)} vezes')

# Em que posição foi digitado o primeiro valor 3
print(f'O numero 3 apareceu na {tuplaNumeroUsuario.index(3)}ª posição')

# Quais foram o números pares.
for i in tuplaNumeroUsuario:
    if i % 2 == 0:
        numerosPares.append(i)
print(f'Os numeros pares são:{numerosPares}')