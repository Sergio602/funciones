def numero_en_rango(numero, rango_inferior, rango_superior):
    if rango_inferior <= numero <= rango_superior:
        return True
    else:
        return False

numero = 5
rango_inferior = 1
rango_superior = 10

if numero_en_rango(numero, rango_inferior, rango_superior):
    print(f"El número {numero} está dentro del rango [{rango_inferior}, {rango_superior}].")
else:
    print(f"El número {numero} está fuera del rango [{rango_inferior}, {rango_superior}].")
