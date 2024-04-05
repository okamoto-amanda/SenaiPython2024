from random import randint

print("O Computador pensou em um numero de 1 a 10")

numeroMaquina = randint(1, 10)
numeroUsuario = int(input("Digite seu palpite: "))
tentativas = 1

print(numeroMaquina)

while numeroUsuario != numeroMaquina:
    tentativas = tentativas + 1
    numeroUsuario = int(input("Palpite INCORRETO. Tente novamente: "))
 
else:
    print(f"O Computador pensou no número {numeroMaquina} e você acertou na {tentativas}ª tentativa. Parabéns! ")
