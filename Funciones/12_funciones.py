def es_palindromo(cadena):
   
    cadena = cadena.replace(" ", "").lower()
    
    
    return cadena == cadena[::-1]


palabra = "Anita lava la tina"
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')