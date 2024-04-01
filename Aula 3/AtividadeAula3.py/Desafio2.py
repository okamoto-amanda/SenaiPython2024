#

velocidade = int(input("Por favor, digite a velocidade do veículo: "))

if velocidade > 80 :
    multaValor = (velocidade - 80) * 7
    print("Você foi multado!")
    print(f"Deve pagar R${multaValor},00 pela infração.")
else :
    print("Tudo certo, boa viagem!")