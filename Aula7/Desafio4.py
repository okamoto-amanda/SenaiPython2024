
numerosUsuario = []
numerosPares = []

while len(numerosUsuario) < 4:
    numerosUsuario.append(int(input("Por favor digite um número: ")))

tuplaNumeroUsuario = tuple(numerosUsuario)                   
print(numerosUsuario)

# Quantas vezes apareceu o valor 9.
print(f'O numero 9 apareceu {tuplaNumeroUsuario.count(9)} vezes')

# Em que posição foi digitado o primeiro valor 3
if 3 in numerosUsuario:
    print(f'O numero 3 apareceu na {tuplaNumeroUsuario.index(3)+1}ª posição')
else:
     print('O numero 3 apareceu não aparece na lista')

# Quais foram o números pares.
for i in tuplaNumeroUsuario:
    if i % 2 == 0:
        numerosPares.append(i)
print(f'Os numeros pares são:{numerosPares}')


##OU#######################################################
numerosUsuario2 = (int(input('Digite um número:'))), (int(input('Digite um número:'))), (int(input('Digite um número:'))), (int(input('Digite um número:')))                 

# Quantas vezes apareceu o valor 9.
print(f'O numero 9 apareceu {numerosUsuario2.count(9)} vezes')

# Em que posição foi digitado o primeiro valor 3
if 3 in numerosUsuario2:
    print(f'O numero 3 apareceu na {numerosUsuario2.index(3)+1}ª posição')
else:
     print('O numero 3 apareceu não aparece na lista')

# Quais foram o números pares.
print(f'Os numeros pares são: ', end='')
for i in numerosUsuario2:
    if i % 2 == 0:
        print(i)
        