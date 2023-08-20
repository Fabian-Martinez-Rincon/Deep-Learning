import math

def distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Ejemplos para probar la función
puntoA = (0, 0)
puntoB = (3, 4)
puntoC = (1, 1)
puntoD = (4, 5)

resultado_AB = distancia(puntoA, puntoB)
resultado_CD = distancia(puntoC, puntoD)

print(resultado_AB, resultado_CD)
#5.0 5.0