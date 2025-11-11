asignaturas = ["matematica", "fisica", "quimica", "naturales", "sociales", "español", "ingles",]

notas = []
for materia in asignaturas:
    nota = input(f"¿Qué nota haz sacado en {materia}?")
    notas.append (nota)

for i in range(len(asignaturas)):
    print("\n--- resultados---")
    print(f"En {asignaturas [i]} has sacado {notas [i]}")