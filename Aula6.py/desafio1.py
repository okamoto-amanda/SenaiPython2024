from random import randint
numeroMaquina = randint(1, 10)
tentativas = 0

numeroUsuario = int(input("O Computador pensou em um numero de 1 a 10\n Digite seu palpite: "))

while numeroUsuario == False:
    tentativas = tentativas + 1
    print("Palpite INCORRETO. Tente novamente: ")
else: 
    print(f"O Computador pensou no número {numeroMaquina} e você acertou. Parabéns! ")
