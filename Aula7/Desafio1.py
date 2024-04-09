
numExtenso = ("zero","um","dois","três","quatro","cinco","seis","sete",
        "oito","nove","dez","onze","doze","treze","catorze","quinze",
        "dezesseis","dezessete","dezoito","dezenove","vinte")

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <= 20:
        print(f"Você digitou: {numExtenso[num]}.")
        break
    else:
        print('Tente novamente.')