#Tener un bucle que va ir iterando sobre un string/lista
#cuando encuentre una exclamacion termina el bucle y nos dice en que posicion esta la exclamacion.


lista="Murcielago! Que bonito!"
contador=0

for letra in lista:
    contador+=1
    if letra=="!":
        print(f"El caracter numero {contador} es una exclamacion!")



#En el zoologico de monstruos hemos visto un monton de criaturas fantasticas.
#Cada vez que alguien veia uno, gritaba el nombreMonstruo! frase! --> "Monstruo! Que miedo!"