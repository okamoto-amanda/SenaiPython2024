#Erro de syntax não conseguimos atribuir except


try:
    for elemento in range(1,10):
        print(elemento)
    
except IndentationError:
    print("Verifique o codigo novamente")