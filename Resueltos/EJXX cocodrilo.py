# FUNCIONES Y DEMAS

import random

def pedirDato(numCocodrilos):
    for setDatos in range(0,numCocodrilos):
        listaNombres.append(crearNombre(numCocodrilos))
        print(f"Dime las estadísticas {listaTiposDatos} para {listaNombres[setDatos]}, el cocodrilo número {setDatos+1}: ")
        listaDientes.append(int(input("")))
        listaLongitud.append(int(input("")))
        listaPeso.append(int(input("")))                            
def crearNombre(numCocodrilos):
    for cocodriloSinNombrar in range(0,numCocodrilos):
        nombreEscogido=random.choice(listaNombresDisponibles)
    return nombreEscogido     
def imprimeEstadisticas(numCocodrilos):
   for cocodrilo in range (0,numCocodrilos):
        grafico=f"""
COCODRILO N{cocodrilo+1}. 
Nombre: {listaNombres[cocodrilo]}
Dientes: {listaDientes[cocodrilo]}
Longitud: {listaLongitud[cocodrilo]}
Peso: {listaPeso[cocodrilo]}
        """
        print(grafico)
        
# CODIGO

listaNombresDisponibles=["Arturo","Rodolfo","Kuma","Hook","Molares","Dandy","Mason","Plumbus","Pablo","Bandido","Escama","KrOkI","Gustave","CrocsInCrocs","Casius","Benito","Rafael"]
listaTiposDatos=["dientes","longitud","peso"]

listaNombres=[]
listaDientes=[]
listaLongitud=[]
listaPeso=[]

numCocodrilos=3

pedirDato(numCocodrilos)
imprimeEstadisticas(numCocodrilos)
