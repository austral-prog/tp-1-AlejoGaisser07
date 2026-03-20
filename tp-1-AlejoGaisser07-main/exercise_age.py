def age():
    """
    Ejercicio 10 - Conversión de Edad a Tiempo

    Dada una edad en años, calcular e imprimir:
    1. La edad en meses (1 año = 12 meses)
    2. La edad en días (1 año = 365 días)
    3. La edad en horas (1 día = 24 horas)
    4. La edad en minutos (1 hora = 60 minutos)
    """
    edad_anos = 25
    año_meses = 12
    año_dias = 365
    dia_horas = 24
    hora_minutos = 60
    edad_meses = edad_anos * año_meses
    print(edad_meses)
    edad_dias = edad_anos * año_dias
    print(edad_dias)
    edad_horas = edad_dias * dia_horas
    print(edad_horas)
    edad_minutos = edad_horas * hora_minutos
    print(edad_minutos)

age()
    
    
