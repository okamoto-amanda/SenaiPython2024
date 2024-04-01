#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
nomeUsuario = input("Este é um programa que faz análise de nomes \nPor favor, digite seu nome completo: ")
listaNomeUsuario = nomeUsuario.split()
primeiroNomeUsuario = listaNomeUsuario[0]
sobrenomeUsuario = listaNomeUsuario[-1]

print(f"Seu nome é:", primeiroNomeUsuario )
print(f"Seu sobrenome é:",sobrenomeUsuario)