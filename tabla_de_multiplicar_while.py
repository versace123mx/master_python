numero = int(input("Ingresa un numero: "))
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        '''print("Found an even number")'''
        continue
    print(f"{numero} X {contador} = {numero * contador}")

