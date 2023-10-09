#Funciones

def numDulces(nNinios,nDulces):
    return numNinios*numMaxDulcesNinio




#Codigo principal

numMaxDulcesNinio=5
numMaxNinios=20
numNinios=int(input('Cuantos ninios vienen? '))
              

if numNinios>numMaxNinios:
    print('No podemos comprar tantos dulces! ')
elif numNinios>0 and numNinios<=numMaxNinios:
    numDulces= numDulces(numNinios,numMaxDulcesNinio)
    print(f'Compraremos {numDulces} dulces')
