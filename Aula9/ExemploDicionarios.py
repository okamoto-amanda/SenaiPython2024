
personagens = [
    {"Nome":"Bob",
     'Sobrenome':'Esponja',
     'Idade':'10'
    },
    {'Nome':'Jhonny',
     'Sobrenome':'Bravo',
     'Idade':'15'
    }
    
]

print(personagens)
print(personagens[0])

primeiroRegistro = personagens[0]
print(primeiroRegistro["Nome"])
print(personagens[0].get("Nome"))