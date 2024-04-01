import random
 
# numero1 = random.randint(1, 10)

# print(numero1)

nota1 = random.randint(1, 10)
nota2 = random.randint(1, 10)
mediaAluno = (nota1 + nota2) / 2
print (f"As notas desse aluno são {nota1} e {nota2} \nSua média é: {mediaAluno}")


if mediaAluno >= 7 :
    print("Aluno aprovado")
else :
    print("Aluno reprovado")
