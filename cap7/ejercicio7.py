number1 = int(input("Ingresa un valor A: "))
number2 = int(input("Ingresa un valor B: "))
if number1 < number2:
    while number1 <= number2:
        if number1 % 2 == 0:
            print(f"El numero {number1} es par")
        else:
            print(f"El numero {number1} es impar")
        number1 += 1
else:
    print(f'El valor (A) debe ser menor a valor (B)')