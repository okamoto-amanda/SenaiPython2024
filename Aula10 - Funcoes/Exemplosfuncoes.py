def calculaArea (largura, altura):
    area = largura * altura
    print(area)
    
def calculoPerimetro (largura, altura):
    perimetro = (2 * largura) + (2 * altura)
    return perimetro



print(calculaArea(largura, altura))
print(calculoPerimetro (5, 3))

def numero():
    return 15 #returne permite salvar valores dentro da funcao

variavelFuncao = numero
print(variavelFuncao()+5)


def calculaPotencia(valor , expoente = 2):
    potencia = valor ** expoente
    (print(potencia))
    
valor = int(input("Digite um valor: "))
calculaPotencia(valor)