numeroUsuario = int(input("Digite um valor: "))

resto = numeroUsuario % 2
print(resto)

if resto == 2 :
    print(f"O valor {numeroUsuario}é par")
else :
    print(f"O valor {numeroUsuario} é impar")