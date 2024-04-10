# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na sua posição
# correta de inserção (sem usar o sort()).

# No final mostre a lista ordenada na tela

numeroUsuario = []
while len(numeroUsuario) < 5:
    numeroUsuario.append(int(input('Numero: ')))

print(numeroUsuario)