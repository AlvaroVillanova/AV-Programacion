#PUNTUADO A 9,33/10

"""
CELIA:
Escrito en una sola línea de código:
def hobbitMenor(edad):
    return edad<33
Si se cumple que a es menor que 33, la operación devuelve True.
En caso contrario devuelve False.
"""

def hobbitMenor(edad):
    if edad<=33:
        puedeRepetir=True
    else:
        puedeRepetir=False
    return puedeRepetir


hobbitNombre1=input("Dime un nombre para este Hobbit: ")
hobbitEdad1=int(input("Dime su edad: "))

hobbitNombre2=input("Dime un nombre para este otro Hobbit: ")
hobbitEdad2=int(input("Dime su edad: "))

hobbitNombre3=input("Dime un nombre para este otro Hobbit: ")
hobbitEdad3=int(input("Dime su edad: "))


puedeRepetir1=False
puedeRepetir2=False
puedeRepetir3=False
puedeRepetirTodos=False

puedeRepetir1=hobbitMenor(hobbitEdad1)
puedeRepetir2=hobbitMenor(hobbitEdad2)
puedeRepetir3=hobbitMenor(hobbitEdad3)

edadTotal=hobbitEdad1+hobbitEdad2+hobbitEdad3
multiplo2=edadTotal%2
multiplo3=edadTotal%3
multiplo5=edadTotal%5

""" 
CELIA:     
Que lio de razonamietno!
* Hay más casos en los que pueden repetir todos.
"""
if edadTotal==60:
    puedeRepetirTodos==True
elif multiplo2==0: 
    puedeRepetir1==True
    if multiplo3==0:
        puedeRepetir2==True
        if multiplo5==0:
            puedeRepetir3==True
elif multiplo2>0:   
    puedeRepetir1==False
    if  multiplo3==0:
        puedeRepetir2==True
        if multiplo5==0:
            puedeRepetir3==True
elif multiplo2>0:
    puedeRepetir1==False
    if multiplo3>0:
        puedeRepetir2==False
        if multiplo5==0:
            puedeRepetir3==True
        else:
            puedeRepetir3==False

if puedeRepetirTodos==True:
    puedeRepetir1=True
    puedeRepetir2=True
    puedeRepetir3=True


print("Puede "+hobbitNombre1+" repetir?: "+str(puedeRepetir1))
print("Puede "+hobbitNombre2+" repetir?: "+str(puedeRepetir2))
print("Puede "+hobbitNombre3+" repetir?: "+str(puedeRepetir3))

if puedeRepetirTodos==True:
    print("Toca repartir la comida!")
elif (puedeRepetir1==False and puedeRepetir2==False and puedeRepetir3==True):
    print("Va a sobrar comida ")
else:
    print("A comer!")