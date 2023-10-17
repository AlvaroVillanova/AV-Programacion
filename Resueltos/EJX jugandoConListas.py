# El string por dentro es un vector: |m|u|r|c|i|e|l|a|g|o|

lista=['m','u','r','c','i','e','l','a','g','o']
listaNum=[0,1,2,3,4,5,6,7,8,9]
palabra="murcielago"
# Se le puede aniadir un caracter asi: lista+="!"

frase= '''Que murcielago


        ...mas bonito!'''


# Para recorrer la palabra podemos usar un bucle:

print ("|", end=" ")
for letra in palabra:
    print(letra, end="|")
print (f"\n{frase}")

contador=0
while contador<10:
    print(f"la letra {palabra[contador]} esta en la posicion {contador}")
    contador+=1

# Con string no se puede porque no tenemos permisos de edicion.

lista[5]="é"

# Pero con lista si se puede.

print(lista)


# De que tipo son cada una de las posiciones d ela lista?

print(f"La lista es de tipo {type(lista[0])}.")
print(f"Cada elemento de la lista es de tipo {type(lista[0])}. ")
      

print(f"La listaNum es de tipo {type(lista[0])}.")
print(f"Cada elemento de la listaNum es de tipo {type(lista[0])}. ")
    
listaNum.append[10] #Esto aniade cosas al final de una lista


#Como mostrar el numero de cosas en una lista

print(f"la lista tiene una longitud de {len(lista)}")

del lista[len(lista)-1
          
nombreAnimal=lista[0:10]


nombreAnimal= lista[0:len(lista)-13+1]