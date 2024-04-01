#Crie um programa que leia o nome de uma cidade e siga se ela começa ou não com o nome “Santo”.
cidadeUsuario = input("Este é um programa que verifica se nome de uma cidade começa com o nome “Santo” \n\nPor favor, digite o nome de qualquer cidade: ")
cidadeVerificacao = cidadeUsuario.split()
cidadeConteudo = "Santo" in cidadeVerificacao[0]

#print (cidadeUsuario, cidadeVerificacao, cidadeConteudo)
print (cidadeConteudo)