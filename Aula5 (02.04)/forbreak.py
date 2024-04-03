#OK
from random import randint

escolhaMaquina = randint(1, 10)

for elemento in range (1,11,1):
    escolhaUsuario = int(input(f"{elemento}º rodada, digite um numero: "))
    
    if escolhaUsuario == escolhaMaquina:
        print("Você venceu!")
        break

    