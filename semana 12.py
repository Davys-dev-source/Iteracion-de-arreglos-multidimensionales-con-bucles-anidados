

ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2


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


for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for s in range(semanas):
        suma = 0
        for d in range(len(dias)):
            suma += temperaturas[i][s][d]
        promedio = suma / len(dias)
        print(f"  Semana {s+1}: promedio = {promedio:.2f}°C")
