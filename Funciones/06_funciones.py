def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos"
    elif numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Ejemplo de uso:
numero = 5
resultado = factorial(numero)

print(f"El factorial de {numero} es {resultado}")

        