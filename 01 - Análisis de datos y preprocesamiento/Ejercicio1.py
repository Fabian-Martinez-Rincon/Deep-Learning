lista = [1, 2, 3, 4, 5]
print(lista)
# [1, 2, 3, 4, 5]

tupla = (1, 2, 3, 4, 5)
print(tupla)
# (1, 2, 3, 4, 5)

conjunto = {1, 2, 3, 4, 5}
print(conjunto)
# {1, 2, 3, 4, 5}

diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

# Clave: a, Valor: 1
# Clave: b, Valor: 2
# Clave: c, Valor: 3

print(diccionario["a"])
# 1