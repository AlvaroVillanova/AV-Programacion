# COCOS 

dibujaCoco1=[" _______"," _^^^^^^"," __/^^^^^/"," _TTTTTTT"]
dibujaCoco2=["/    *  *_______","/    o  o_______","/    >  <_______","/ ---O--O_______"]
dibujaCoco3=["  _____vvvvvvvvv/","  _____uuuuuuuuu/","  _____wwwwwwwww/","  _____---------/"]


# FUNCIONES Y DEMAS


import random

def numeroAleatorio(num):
    numero=random.randrange(0,num)
    return numero
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
Nombre: {listaNombres[cocodrilo]}         {dibujaCoco1[numeroAleatorio(4)]}
Dientes: {listaDientes[cocodrilo]}             {dibujaCoco2[numeroAleatorio(4)]}
Longitud: {listaLongitud[cocodrilo]}           {dibujaCoco3[numeroAleatorio(4)]}
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

print("\n"*100)
pedirDato(numCocodrilos)
imprimeEstadisticas(numCocodrilos)


