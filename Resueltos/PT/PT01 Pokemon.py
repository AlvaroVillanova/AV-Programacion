#PUNTUADO A 7,67/1O


import random

def fraseAleatoria():
    frases = [
        "¡El ganador de la batalla es increible!",
        "¡La victoria ha sido para el mejor Pokémon!",
        "¡Nuestro ganador a triunfado en la batalla!",
        "¡Enhorabuena al Pokémon ganador!",
        "¿Quién ganará la próxima vez?"
    ]
    fraseElegida = random.choice(frases)
    return fraseElegida

#Bienvenida
print("Bienvenido al Coliseo Pokemon. Primero escoge los pokemons que van a luchar ")
#Primer Pokemon:
poke1type=input("Escoge el tipo de elemento de tu primer Pokemon (Agua/Fuego/Planta): ")
poke1name=input("Escoge el nombre de tu primer pokemon: ")
poke1lvl=int(input("De que nivel es el primer pokemon?(Del 1 al 50) "))
#Segundo Pokemon:
print("Ahora el segundo pokemon...")
poke2type=input("Escoge el tipo de elemento del segundo Pokemon (Agua/Fuego/Planta): ")
poke2name=input("Escoge el nombre del segundo pokemon: ")
poke2lvl=int(input("De que nivel es el segundo pokemon?(Del 1 al 50) "))

#A pelear:
print("Hoy se enfrentan en el coliseo: ")
print(str(poke1name)+" el pokemon de nivel "+str(poke1lvl)+" de tipo "+str(poke1type))
print("VS")
print(str(poke2name)+" el pokemon de nivel "+str(poke2lvl)+" de tipo "+str(poke2type))
print("A luchar!!!")
print("...")
print("...")
print("El ganador es...")


if (poke1type==poke2type and poke1lvl>poke2lvl):
    print("Gana "+poke1name+str(fraseAleatoria()))
elif (poke1type==poke2type and poke1lvl<poke2lvl):
    print("Gana "+poke2name+str(fraseAleatoria()))
elif (poke1type=="Fuego" and poke2type!="Fuego"):
    if  (poke2lvl-poke1lvl>=10):
        print("Gana "+str(poke2name)+str(fraseAleatoria()))
    elif():
        print("Gana "+str(poke1name)+str(fraseAleatoria()))
elif(poke2type=="Fuego" and poke1type!="Fuego"):
    if (poke1lvl-poke2lvl>=10):
        print("Gana "+str(poke1name)+str(fraseAleatoria()))
    elif():
        print("Gana "+str(poke2name)+str(fraseAleatoria()))
else: 
    print("Han empatado... Que extraño!")   



if poke1type==poke2type:
    print("La pelea fue justa!")
else:
    print("La pelea no fue muy justa!")