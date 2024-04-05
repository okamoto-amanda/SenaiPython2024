from random import randint
numeroMaquina = randint(1, 10)

numeroUsuario = int(input("O Computador pensou em um numero de 1 a 10\n Digite seu palpite: "))
tentativas = 0

while True:
    if numeroUsuario != numeroMaquina:
        tentativas = tentativas + 1
        print("Palpite INCORRETO. Tente novamente: ")
    else: 
        print(f"O Computador pensou no número {numeroMaquina} e você acertou. Parabéns! ")
