def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12
    lista = [num1, num2, num3, num4]
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    rango = maximo - minimo
    print(promedio)
    print(maximo)
    print(minimo)
    print(rango)

statistics()