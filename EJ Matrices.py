otraMatriz=[[9,8,7],[6,5,4],[3,2,1]]
matriz=[[1,2,3],[4,5,6],[7,8,9]]

#   0  1  2
#0  1  2  3
#1  4  5  6
#2  7  8  9

# EJ1 Sumar todos los elementos de la matriz

suma=0

for fila in matriz:
    for columna in fila:
        suma+=columna

print("1. ")
print(suma)

# EJ2 Sumar elementos de fila indicada

filaIndicada=1

def sumarFilasSeleccionadas(matriz,filaIndicada):
    suma=0
    for fila in range(len(matriz)):
        if fila==filaIndicada:
            suma+=matriz[filaIndicada][fila]
    return suma
print("2. ")
print(sumarFilasSeleccionadas(matriz,filaIndicada))

# EJ3 Sumar elementos de columna indicada

columnaIndicada=1

def sumarColumnasSeleccionadas(matriz,columnaIndicada):
    suma=0
    for fila in range(len(matriz)):
            suma+=matriz[fila][columnaIndicada]
    return suma
print("3. ")
print(sumarColumnasSeleccionadas(matriz,columnaIndicada))


# EJ4 Sumar elementos que estan en posiciones pares

def sumarPosicionesPares(matriz):
    suma=0
    i=0
    j=0
    for fila in matriz:
        j=0
        for columna in fila:
            parOImpar=i+j
            if parOImpar%2==0:
                suma+=matriz[i][j]
            j+=1
        i+=1
    return suma

print("4. ")
print(sumarPosicionesPares(matriz))


# EJ5 Sumar elementos que estan en posiciones impares

def sumarPosicionesImpares(matriz):
    suma=0
    i=0
    j=0
    for fila in matriz:
        j=0
        for columna in fila:
            parOImpar=i+j
            if parOImpar%2!=0:
                suma+=matriz[i][j]
            j+=1
        i+=1
    return suma

print("5. ")
print(sumarPosicionesImpares(matriz))


# EJ6 Rellenar una matriz con cada fila su numero de fila

matrizAux=[[1,2,3],[4,5,6],[7,8,9]]




# Rellenar una matriz con cada columna su numero de columna
# Sumar los elementos que se encuentran en la diagonal principal:
# Rellenar matriz con 0s en las posiciones pares y 1s en las impares
# Sumar todos los elementos pares:

def sumarElementosPares(matriz):
    suma=0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j]%2==0:
                suma+=matriz[i][j]
    return suma

print("X.")
print(sumarElementosPares(matriz))
