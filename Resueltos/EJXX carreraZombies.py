"""# Carrera de Zombies
Recopila la información de tres Zombies: Su color, su longitud de salto y su frecuencia de salto.

¿Qué zombie ganaría una carrera de 50 metros? ¿Y de 100 metros?
[Crea una función a la que le pases los metros que tenga la carrera y las características de los zombies y te devuelva quién gana]

Esa función sería muy compleja y cambiaría dependiendo del número de zombies que participaran en la carrera: Crea una función a la que le pases la info de un solo zombie y te indique en qué segundo llegaría cada uno de los zombiens a la meta.
Al comparar los segundos que tarda cada uno de los zombies podremos saber cuál es el ganador.
```
# Info sobre el zombie.
...
El Zombie Rojo tarda 30 segundos.
El Zombie Azul tarda 27 segundos.
El Zombie Verde tarda 33 segundos.

Gana el Zombie Azul.
```
¿Podemos generar la información de los tres zombies de forma aleatoria? [La longitud de salto debe ser entre 3 y 7 metros y la frecuencia de salto entre 5 y 15 segundos.]
```
...
El Zombie Rojo salta 3 metros cada 10 segundos.
El Zombie Azul salta 2 metros cada 3 segundos.
El Zombie Verde salta 1 metro cada 2 segundos.
```
Genera aleatoriamente cinco rondas con tres zombies cada una [cada zombie de un color, que representa su equipo] ¿Qué equipo ha ganado más rondas?
```
La primera ronda la gana el Zombie Azul.
La segunda ronda la gana el Zombie Rojo.
La tercera ronda la gana el Zombie Rojo.
La cuarta ronda la gana el Zombie Verde.
La quinta ronda la gana el Zombie Rojo.

Ha ganado el equipo Rojo.
"""
import random 

def pedirLongitudSalto():
    return random.randrange(3,7+1)


def pedirFreqSalto():
    return random.randrange(5,15+1)


def pedirColorZombie():
    colorZombies=[random.choice(0,3)]
    return colorZombies

def calculoCarrera(metrosCarrera):
    longSalto=pedirLongitudSalto()
    freqSalto=pedirFreqSalto()
    resultadoZombie=metrosCarrera/(longSalto/freqSalto)
    return resultadoZombie

#Define los colores de los tres equipos

colorEquipo1="Rojo"
colorEquipo2="Azul"
colorEquipo3="Verde"

#Listas 

colores=[colorEquipo1,colorEquipo2,colorEquipo3]
colorZombie=[]
resultadoZombie=[]





metrosCarrera=50    #int(input("De cuantos metros es la carrera?"))
zombiesParticipantes=3       #int(input("Cuantos zombies van a participar? "))
numRondas=5     #int(input("Cuantas rondas van a jugar? "))

contador=0

for ronda in numRondas:
    for zombie in zombiesParticipantes:
        resultadoCarrera=calculoCarrera(metrosCarrera)
        print(f"Corredor num. {contador+1}, Zombie {colorZombies[contador]}. Completa el circuito en {resultadoCarrera} segs! ")
        contador+=1



#Definimos ganador


test=f"""
metrosCarrera: {metrosCarrera}       zombiesParticipantes: {zombiesParticipantes}
colorZombies: {pedirColorZombie()}



"""
print(test)
    




anuncioCarrera="""
En la carrera de hoy participan:

"""

