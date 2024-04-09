
timesBrasileirao = 'Amazonas','América-MG','Avaí','Botafogo-RP','Brusque','CRB','Ceará','Chapecoense','Coritiba','Goiás','Guarani','Ituano','Mirassol','Novorizontino','Operário-PR','Paysandu','Ponte Preta','Santos','Sport','Vila Nova'

# Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Santos.

print(timesBrasileirao[5])
print(timesBrasileirao[16:])

ordemTimes = timesBrasileirao
ordemTimes = sorted(timesBrasileirao)
print(ordemTimes)


