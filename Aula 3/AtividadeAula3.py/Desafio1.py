from random import randint

print("Este é um jogo que te desafia a adivinhar um número aleatório de 0 a 5")
numeroAleatorio = randint(0,5)
numeroUsuario = int(input("Tente adivinhar qual número o computador escolheu: "))

if numeroUsuario == numeroAleatorio :
    print("Parabéns! Você venceu.")
else :
    print(f"Não foi dessa vez!\nO número escolhido foi {numeroAleatorio}")