
timesBrasileirao = 'Amazonas','América-MG','Avaí','Botafogo-RP','Brusque','CRB','Ceará','Chapecoense','Coritiba','Goiás','Guarani','Ituano','Mirassol','Novorizontino','Operário-PR','Paysandu','Ponte Preta','Santos','Sport','Vila Nova'

# Apenas os 5 primeiros colocados
print(timesBrasileirao[:5])

#Os últimos 4 colocados da tabela
print(timesBrasileirao[16:])

# Uma lista com os times em ordem alfabética.
ordemTimes = sorted(timesBrasileirao)
print(ordemTimes)

# Em que posição na tabela está o time do Santos.
posicaoSantos = timesBrasileirao.index('Santos')
print(posicaoSantos)
