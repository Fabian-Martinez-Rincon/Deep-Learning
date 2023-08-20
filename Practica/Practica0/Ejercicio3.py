def eliminar_duplicados(lista):
    return list(dict.fromkeys(lista))

# Ejemplos para probar la función
ejemplo1 = [1, 2, 3, 1, 2, 4, 5]
ejemplo2 = ["a", "b", "a", "c", "d", "b"]
ejemplo3 = [True, False, True, True]

resultado1 = eliminar_duplicados(ejemplo1)
resultado2 = eliminar_duplicados(ejemplo2)
resultado3 = eliminar_duplicados(ejemplo3)

print(resultado1, resultado2, resultado3)
# [1, 2, 3, 4, 5] ['a', 'b', 'c', 'd'] [True, False]