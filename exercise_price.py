def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100
    precio_impuesto = precio_base * (21/100)
    subtotal = precio_base + precio_impuesto
    precio_propina = subtotal * 0.1
    precio_total = subtotal + precio_propina
    print(precio_impuesto)
    print(subtotal)
    print(precio_propina)
    print(precio_total)

price()