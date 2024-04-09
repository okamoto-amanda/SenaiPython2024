
numerosUsuario = []
while len(numerosUsuario) < 4:
    numerosUsuario.append(int(input("Por favor digite um número: ")))

tuplaNumeroUsuario = tuple(numerosUsuario)                   
print(numerosUsuario)

# Quantas vezes apareceu o valor 9.
print(tuplaNumeroUsuario.count(9))

# Em que posição foi digitado o primeiro valor 3
print(tuplaNumeroUsuario.index(3))

# Quais foram o números pares.
for i in tuplaNumeroUsuario:
    if i % 2 == 0:
        print(i)