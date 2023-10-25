"""

Generea aleatoriamente cinco rondas con tres zombies cada una
cada zombie es de un color, que representa su equipo

"""

import random

#FUNCIONES


def solicitarNombreAEquipo():
    return input("Dime el color del equipo: '")

def rellenarConDatosAleatorios():
    longSalto=random.randrange(3,7+1)
    listaLongSaltoZombies.append(longSalto)
    frecSalto=random.randrange(5,15+1)
    listaFreqSaltoZombies.append(frecSalto)




#CODIGO PRINCIPAL

numEquipos=3
listaEquipos=[]
listaFreqSaltoZombies=[]
listaLongSaltoZombies=[]

for equipo in range(numEquipos):
    listaEquipos.append(solicitarNombreAEquipo())


