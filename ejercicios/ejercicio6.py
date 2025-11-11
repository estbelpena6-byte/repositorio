asignaturas =  ["matematica", "fisica", "quimica", "naturales", "sociales", "español", "ingles",]

reprobadas = []

for materia in asignaturas:
    nota = float(input(f"¿Que nota has sacado en {materia}?"))

    if nota < 60:
        reprobadas.append(materia)

print("\n --- asignaturas que tienes que repetir ---")
if len(reprobadas) == 0:
    print("¡felicidades! has aprobado todas las asignaturas")
else:
    for materia in reprobadas:
        print(materia)