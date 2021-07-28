numero = int(input("Ingresa un numero: "))
for contador in range(1,11):
    if contador == 5:
        '''print("Found an even number", num)'''
        continue
    print(f"{numero} X {contador} = {numero * contador}")