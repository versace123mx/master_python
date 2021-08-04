a = 1
aprobatoria = 0
reprobatoria = 0

while a <= 10:
    calificacion = float(input(f"Ingresa calificacion para alumno {a}: "))

    if calificacion >= 6:
        aprobatoria += 1
    else:
        reprobatoria += 1
    a += 1

print(f'Alomnos aprobados: {aprobatoria}')
print(f'Alomnos reprobados: {reprobatoria}')