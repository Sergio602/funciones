def elementos_unicos(lista):
    return list(set(lista))
mi_lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = elementos_unicos(mi_lista)

print("Lista original:", mi_lista)
print("Lista con elementos únicos:", lista_sin_duplicados)
