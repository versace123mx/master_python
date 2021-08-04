number1 = int(input("Ingresa un valor A: "))
number2 = int(input("Ingresa un valor B: "))
if number1 < number2:
    while number1 <= number2:
        print(f"{number1}")
        number1 +=1
else:
    print(f'El valor (A) debe ser menor a valor (B)')