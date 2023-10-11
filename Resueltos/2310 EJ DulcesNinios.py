"""
CONTEXTO: Estás organizando una fiesta de Halloween y quieres 
calcular cuántos dulces necesitas comprar para los niños que 
vendrán a tu casa.



CASO 1: Tenemos 500 dulces y vamos a repartirlos entre niños que 
cogen un número aleatorio de caramelos.

"""
#Libs, functions and stuff

import random

def numDulcesPorNinioF():
    numDulcesRandom=random.randint(1,5)
    while numDulcesTotal<numDulcesRandom:
        numDulcesRandom-=1
    return numDulcesRandom
    

#Body

numDulcesTotal=500
numNiniosAlimentados=0

while numDulcesTotal>0:
    numDulcesPorNinio=numDulcesPorNinioF()
    print("Ha venido un ninio. Se lleva "+str(numDulcesPorNinio)+" dulces")
    print("Quedan "+str(numDulcesTotal)+" dulces a repartir.")
    numDulcesTotal-=numDulcesPorNinio
    numNiniosAlimentados+=1

print("Bien! Hemos alimentado "+str(numNiniosAlimentados)+" nineos.")

