# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final serão
# exibidos todos os valores únicos digitados, em ordem
# crescente.

listaUsuario = []

while True:
    NumeroUsuario = (input("Digite N para sair \nOu digite um novo número: ")).upper()
    if NumeroUsuario == 'N':
        break
    if  NumeroUsuario not in listaUsuario :
        listaUsuario.append(NumeroUsuario)
    else:
        print('O numero digitado ja existe\n')
print(f'Os números da lista são:{sorted(listaUsuario)}')
