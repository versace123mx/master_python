def tabla(num):
    print(f"Tabla del # {num}")
    for contador in range(1,11):
        print(f'{num} X {contador} = {num*contador}')
        if contador == 10:
            print('\n')


for contador in range(1,11):
    tabla(contador)