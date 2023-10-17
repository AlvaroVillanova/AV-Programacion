# El string por dentro es un vector: |m|u|r|c|i|e|l|a|g|o|

lista=['m','u','r','c','i','e','l','a','g','o']
palabra="murcielago"
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
print(lista)


