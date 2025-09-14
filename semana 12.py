# Listas de ciudades, días de la semana y número de semanas
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2

# Matriz de temperaturas: ciudades -> semanas -> días
temperaturas = [
    [  # Quito
        [18, 20, 22, 19, 21, 20, 18],  # Semana 1
        [19, 21, 23, 22, 20, 19, 18]   # Semana 2
    ],
    [  # Guayaquil
        [28, 29, 30, 31, 32, 30, 29],  # Semana 1
        [29, 30, 31, 32, 33, 31, 30]   # Semana 2
    ],
    [  # Cuenca
        [15, 16, 17, 15, 16, 17, 15],  # Semana 1
        [16, 17, 18, 17, 16, 17, 16]   # Semana 2
    ]
]

# --- Parte 1: Mostrar promedio por semana ---
print("Promedios por semana:\n")
for i, ciudad in enumerate(ciudades):
    print(f"Ciudad: {ciudad}")
    for s in range(semanas):
        suma = sum(temperaturas[i][s])
        promedio = suma / len(dias)
        print(f"  Semana {s+1}: promedio = {promedio:.2f}°C")

# --- Parte 2: Función para calcular promedio total por ciudad ---
def promedio_total_ciudad(ciudades, temperaturas):
    """
    Calcula la temperatura promedio total de cada ciudad considerando todas sus semanas.

    Parámetros:
    - ciudades: lista de nombres de ciudades
    - temperaturas: lista 3D con temperaturas [ciudad][semana][día]

    Retorna:
    - diccionario con ciudad como clave y temperatura promedio como valor
    """
    promedios = {}
    for i, ciudad in enumerate(ciudades):
        total = 0
        dias_totales = 0
        for semana in temperaturas[i]:
            total += sum(semana)
            dias_totales += len(semana)
        promedios[ciudad] = round(total / dias_totales, 2)
    return promedios

# --- Parte 3: Mostrar promedio total de cada ciudad ---
print("\nPromedios totales por ciudad:")
promedios = promedio_total_ciudad(ciudades, temperaturas)
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio}°C")

