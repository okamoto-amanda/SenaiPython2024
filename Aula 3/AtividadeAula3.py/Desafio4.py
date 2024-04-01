# Faça um programa que leia três números e mostre qual é o
# maior e qual é o menor. 

print("Por favor digite 3 valores que vou te mostrar qual deles é o maior e qual é o menor")
Aa = int(input("1º valor: "))
Bb = int(input("2º valor: "))
Cc = int(input("3º valor: "))

if Aa > Bb and Aa > Cc:
    maior = Aa
elif Bb > Aa and Bb > Cc:
    maior = Bb
else:
    maior = Cc
#print(maior)

if Aa < Bb and Aa < Cc:
    menor = Aa
elif Bb < Aa and Bb < Cc:
    menor = Bb
else :
    menor = Cc
#print(menor)
print(f"O maior entre eles é o {maior}\nO menor entre eles é o {menor}")