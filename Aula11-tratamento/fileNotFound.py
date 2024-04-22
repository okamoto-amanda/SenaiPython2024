try:
    with open("data.txt", "r") as arquivo:
        conteudo = arquivo.read()
        
except FileNotFoundError:
    print("O arquivo nao existe")
finally: 
    print("Fim")
    