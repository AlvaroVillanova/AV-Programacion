"""
# Monstruos visualizados
En el zoológico de monstruos hemos visto un montón de criaturas fantásticas.

Cada vez que alguien veía uno, gritaba el nombreMonstruo! frase! -> 
                                                        "Monstruo! Que feo!"
Hemos hecho una lista de todas las veces que ha gritado la gente.
Tenemos que sacar de esa lista, otra lista con los tipos de monstruo que hemos 
visualizado.
""" 

listaDeExclamaciones = ["Bruja! Que fea!","Vampiro! Que miedo!","Lobo! Que adorable!","Zombie! Corre!"]
listaMonstruos = []

# Empezamos extrayendo de "Bruja! Que fea!" todo lo que haya antes de la exclamación

"""
frase = "Bruja! Que fea!"
signoEncontrado = False
contador = 0
print(frase)
while not signoEncontrado:
    if frase[contador] == "!":
        signoEncontrado = True
    contador += 1
print(f"He encontrado la ! en la posición {contador-1}")
"""

for exclamacion in listaDeExclamaciones:
    signoEncontrado = False
    contador = 0
    print(exclamacion)
    while not signoEncontrado:
        if exclamacion[contador] == "!":
            signoEncontrado = True
        contador += 1  
    contador-=1
    
    
    #Estas dos lineas tontas
    
    bicho=exclamacion[0:contador]
    listaMonstruos.append(bicho)

print(f"Wow! hemos visto: {listaMonstruos[0]}, {listaMonstruos[1]}, {listaMonstruos[2]} y {listaMonstruos[3]}. ")

    
