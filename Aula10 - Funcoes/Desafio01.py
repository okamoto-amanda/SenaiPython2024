
#se possivel, declarar as variaveis primeiro 

largura = int(input("Digite a largura: "))
comprimento = int(input("Digite a altura: "))


def area(largura , comprimento ):
    area = largura * comprimento
    return area #Serve para que o valor seja um valor global


area(largura, comprimento)
print(f"A area do terreno é igual a {area(largura, comprimento)} m²")
