def contar_letras_mayusculas_y_minusculas(cadena):
    mayusculas = 0
    minusculas = 0

    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1

    return mayusculas, minusculas
cadena = "Ejemplo de Cadena con Mayúsculas y minúsculas."

mayusculas, minusculas = contar_letras_mayusculas_y_minusculas(cadena)

print(f"Número de letras mayúsculas: {mayusculas}")
print(f"Número de letras minúsculas: {minusculas}")
