# Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na sua posição
# correta de inserção (sem usar o sort()).

# No final mostre a lista ordenada na tela

numeroUsuario = []

for i in range (0,5):
    n = int(input('Digite um numero: '))
    
    if i == 0 or n > numeroUsuario[-1]:
        numeroUsuario.append(n)
        print("Adicionado ao final da lista")
        
    else:
        pos = 0
        while pos < len(numeroUsuario):
            if n <= numeroUsuario[pos]:
                numeroUsuario.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista')
                break
        pos += 1
print(f"Os valores da lista são {numeroUsuario}")
#nao finalizado


# lista = [] #10

# for c in range(0,5):    
#     n = int(input("Digite um valor: ")) #10 ,1, 15,20,7   c=2

#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#         print('Adicionado ao final da lista')
#     else:
#         pos = 0
#         while pos < len(lista):  # 2<2
#             if n <= lista[pos]: # 15<10
#                 lista.insert(pos,n)# lista = [1,10,15,20]
#                 print(f"Adicionado na posição {pos} da lista")
#                 break
#             pos += 1

# print(f"Os valores digitados em ordem foram {lista}")