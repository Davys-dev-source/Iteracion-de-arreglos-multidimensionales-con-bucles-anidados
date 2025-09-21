# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento a partir del monto total y el porcentaje.
    
    :param monto_total: Monto total de la compra
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (10% por defecto)
    :return: Monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
def main():
    # Primera llamada: solo monto total, se aplica descuento por defecto (10%)
    monto1 = 150
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Compra 1: Monto total = ${monto1}")
    print(f"Descuento aplicado = ${descuento1}")
    print(f"Monto final a pagar = ${monto_final1}\n")
    
    # Segunda llamada: monto total y porcentaje de descuento personalizado
    monto2 = 200
    porcentaje2 = 20
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2
    print(f"Compra 2: Monto total = ${monto2}")
    print(f"Descuento aplicado ({porcentaje2}%) = ${descuento2}")
    print(f"Monto final a pagar = ${monto_final2}")

# Ejecutar programa principal
if __name__ == "__main__":
    main()


