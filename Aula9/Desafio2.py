# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultado aleatórios. Guarde esses resultados em um
# dicionário . No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior numero no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogada1 = randint(1, 6)+randint(1, 6)
jogada2 = randint(1, 6)+randint(1, 6)
jogada3 = randint(1, 6)+randint(1, 6)
jogada4 = randint(1, 6)+randint(1, 6)
#Colocando em ordem 

jogo = {
    'jogador1' : jogada1,
    'jogador2' : jogada2,
    'jogador3' : jogada3,
    'jogador4' : jogada4,
}

print(jogo)
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)


vencedor = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(vencedor)
