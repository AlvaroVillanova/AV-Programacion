
# Recuerda utilizar FUNCIONES cada vez que quieras reutilizar el código de un ejercicio a otro!
#Los números de los ejercicios pueden cambiar...



def solicitarPalabras(numPalabras):
    listaPalabras.clear()
    contadorEnunciado=0
    for palabra in range(0,numPalabras):
        nuevaPalabra=input(f"Dime la {contadorEnunciado+1}ª palabra: ")
        listaPalabras.append(nuevaPalabra)
        contadorEnunciado+=1
    return listaPalabras
def solicitarNumeros(numNumeros):
    listaNumeros.clear()
    contadorEnunciado=0
    for numero in range(0,numNumeros):
        nuevoNumero=int(input(f"Dime un {contadorEnunciado+1}º numero: "))
        listaNumeros.append(nuevoNumero)
        contadorEnunciado+=1
    return listaNumeros


# LISTAS:

listaDebug=["bug","glitch","crash","poof"]
listaNumerosDebug=[4,7,5,9,2,1,8,6]

listaNumeros=[]
listaNumeros2=[]
listaElementos=[]
listaPalabras=[]

"""

# --------- EJ Crear ----------
# 1.- Crea una lista de 5 palabras directamente en el código.

listaPalabras=["Perro","Gato","Hurón","Cobaya","Poltergeist"]
print(listaPalabras)

# 2.- Crea una lista de 5 palabras, solicitándolas por consola.

numPalabras=5
listaPalabras=solicitarPalabras(numPalabras)
print(listaPalabras)


# 3.- Solicita de cuántas palabras quieres que sea una lista.
# Crea una lista de ese número de palabras, solicitándolas por consola.

numPalabras=int(input("De cuantas palabras quieres esta lista?: "))
listaPalabras=solicitarPalabras(numPalabras)
print(listaPalabras)

# 4.- Crea una lista que contenga los números del 1 al 20

listaNumeros.clear()
totalNumeros=20
for numero in range(1,totalNumeros+1):
    listaNumeros.append(numero)
print(listaNumeros)


# 5.- Solicita dos números por consola.
#Crea una lista que contenga los números comprendidos entre esos dos, ambos incluidos.
#Asegurate de que funcione aunque el primer numero introducido sea menor que el primero.

listaNumeros=solicitarNumeros(2)
if listaNumeros[0]>listaNumeros[1]:
    listaNumeros.sort()
for unidad in range(listaNumeros[0],listaNumeros[1]+1):
    listaNumeros2.append(unidad)
print(listaNumeros2)
    


# --------- EJ Borrar --------
# 6.- Elimina todos los elementos de una lista mostrando por pantalla:
# Se ha eliminado el elemento *numero del elemento* de la lista: *elemento*


listaPalabras=["Sombrero","Camiseta","Pantalon","Zapatos","Guantes"]

contadorElemento=0
for palabra in listaPalabras:
    print(f"Se ha eliminado el elemento {contadorElemento} de la lista: {listaPalabras[contadorElemento]}")
    contadorElemento+=1
listaPalabras.clear()
    



# --------- EJ Mostrar --------
# 7.- Muestra todos los elementos de una lista separados por espacios.

for bugs in listaDebug:
    print("")
    for letras in bugs:
        print(letras, end=" ")



# 8.- Muestra todos los elementos de una lista mostrando por pantalla:
# El elemento número *numero del elemento* de la lista *nombre de la lista* es: *elemento*.


contadorDebug=0
numElementos=len(listaDebug)
for elementoLista in range(numElementos):
    print(f"El elemento número {contadorDebug} de la lista {nombre de la lista} es: {elemento}.")


# --------- EJ Buscar ---------
# 9.- Solicita por consola un número.
# Devuelve el elemento que hay en la posición indicada por número.

listaPalabras=["perro","gato","huron"]
nPalabra=int(input("Numero de objeto en la lista a mostrar? "))
print(listaPalabras[nPalabra+1])



# 10.- Solicita por consola un elemento.
# Lo busca en la lista: Devuelve si está en la lista o no.

listaPalabras=["perro","gato","huron"]
palabraABuscar=input("Que palabra quieres buscar en la lista? ")
coincidencia=0

for palabra in listaPalabras:
    if palabra == palabraABuscar:
        coincidencia=1

if coincidencia==1:
    print("Tu palabra SI esta en la lista. ")
else:
    print("Tu palabra NO esta en la lista. ")



# 11.- Solicita por consola un elemento.
#Lo busca en la lista: Devuelve la posición que tiene dentro de la lista.

listaPalabras=["perro","gato","huron"]
palabraABuscar=input("Que palabra quieres buscar en la lista? ")
coincidencia=0
contadorPalabra=0

for palabra in listaPalabras:
    if palabra == palabraABuscar:
        coincidencia=1
        palabraGanadora=contadorPalabra
    contadorPalabra+=1   
    

if coincidencia==1:
    print(f"Tu palabra esta en la lista en la posicion: {palabraGanadora} ")
else:
    print("Tu palabra NO esta en la lista. ")



# --------- EJ Modificar --------

# 12.- Solicita por consola un número y un elemento.
# Cambia el elemento que hay en la posición indicada por número por el nuevo elemento.

print("Inserta el nombre de un elemento y un numero: ")
listaElementos.append(solicitarPalabras(1))
listaElementos.append(solicitarNumeros(1))

"""
# 13.- Solicita por consola un numero.
# Lo busca en la lista de números: Todos los que sean mayores que ese número se cambian a ese número.

numMenor=listaNumerosDebug[0]
contador=0
for numero in listaNumerosDebug:
    if numero < numMenor:
        numMenor=listaNumerosDebug[contador]
    contador+=1

print(numMenor)

# 14.- Solicita por consola dos numeros.
# Lo busca en la lista de números: Todos los que sean mayores que el mayor de los números se cambian por él. Todos los que sean menores que el menor de los números se cambian por él.

# 15.- Solicita por consola dos numeros.
# Lo busca en la lista de números: Todos los que sean mayores que el mayor de los números se dividen entre dos hasta dejar de serlo. Todos los que sean menores que el menor de los números se multiplican por dos hasta dejar de serlo.

# 16.- Solicita por consola un numero.
# Lo busca en la lista de números: Todos los que sean mayores que ese número se cambian a ese número.

# 17.- Solicita por consola dos numeros.
# Lo busca en la lista de números: Todos los que sean mayores que el mayor de los números se cambian por él. Todos los que sean menores que el menor de los números se cambian por él.

# 18.- Solicita por consola dos numeros.
#Lo busca en la lista de números: Todos los que sean mayores que el mayor de los números se dividen entre dos hasta dejar de serlo. Todos los que sean menores que el menor de los números se multiplican por dos hasta dejar de serlo.

# 19.- Busca el número más grande y el más pequeño e intercambia sus posiciónes.

# ---------------- Calcular -----------------
# 20.- Suma todos los números de una lista.
"""
sumaTotal=0
contador=0
for numero in listaNumerosDebug:
    sumaTotal+=(listaNumerosDebug[contador])
    contador+=1

print(sumaTotal)

# 21.- Multiplica todos los elementos de una lista.

multiplicacionTotal=1
contador=0
for numero in listaNumerosDebug:
    multiplicacionTotal = multiplicacionTotal*listaNumerosDebug[contador]
    contador+=1

print(multiplicacionTotal)

# 22.- Haz la media de todos los elementos de una lista.

sumaTotal=0
contador=0
for numero in listaNumerosDebug:
    sumaTotal+=(listaNumerosDebug[contador])
    contador+=1
mediaTotal=sumaTotal/contador

print(mediaTotal)

# 23.- Recorre una lista sumando los números que la componen. Cuando estos elementos sumen 21: para.

sumaTotal=0
contador=0
for numero in listaNumerosDebug:
    if  sumaTotal<21:
        sumaTotal+=(listaNumerosDebug[contador])
        contador+=1
print(f"Hemos parado en el elemento {contador} de la lista, suma total: {sumaTotal} ")
    
"""


# ---------------- Ordenar listas -------------

# 24.- Ordena de menor a mayor una lista de números de la siguiente forma:
# - Busca el número más pequeño.
# - Añádelo a una lista nueva.
# - Elimínalo de la lista actual.
# - Al terminar guarla la lista nueva ordenada en la lista antigua desordenada.


def obtenerNumeroMenor(listaNumeros):
    numMenor=listaNumeros[0]
    for numero in listaNumeros:
        if numero<numMenor:
            numMenor=numero
    return numMenor

def clonarLista(origen,destino):
    for element in origen:
        destino.append(element)

listaNumerosDebug=[4,7,5,9,2,1,8,6,113,543,65,23,34,65,2,87,34,23,54,12,87]
listaNumerosAux=[]


for indice in range(len(listaNumerosDebug)):
    numMenor=obtenerNumeroMenor(listaNumerosDebug)
    listaNumerosAux.append(numMenor)
    listaNumerosDebug.remove(numMenor)

#listaNumerosDebug.append(listaNumerosAux)
clonarLista(listaNumerosAux,listaNumerosDebug)

print(f"Hey esta es tu nueva lista ordenada. {listaNumerosDebug}")





# 25.- Ordena de mayor a menor.



