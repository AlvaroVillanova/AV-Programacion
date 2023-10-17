"""
Nos hemos encontrado un tesorro mágico en la guarida de un 
temible dragón. 
A los dragones les encantan las cosas que brillan y por eso 
prefería tener muchísimas monedas mejor que pocas pero de 
mayor cantidad, por eso tenía un total de 4765 Knuts.

Cada Sickle son 29 Knuts.
Cada Galeón son 17 Sicles.

#1. Calcula matemáticamente el valor con el número mínimo de
Galeones, Sickles y Knuts posibles. [Utilizando el módulo]

#2. Con solo 493 Knuts representa en forma de marcador 
                            *marcador puntuacion papel reloj*
el proceso de ir añadiendo Knuts hasta llegar a 29 y que estos
se combiertan en una moneda de Sickle y el proceso de ir 
consiguiendo Sickles hasta llegar al Galeón.
""" 



#EJERCICIO 1

knutsComienzo=523
sickle=knutsComienzo//29
knut=knutsComienzo%29

galeon=sickle//17
sickle=sickle%17

print(f"Tenemos {knutsComienzo} knut. Cuanto será al cambio?")
print(f"Al cambio son {galeon} galeones, {sickle} sickle y {knut} knut.")



#EJERCICIO 2

#knutsComienzo=4765   
#knutsComienzo=int(input("Cuantos knuts tenemos? "))

knut=knutsComienzo
sickle=0
galeon=0

while knut>28:
    knut-=29
    sickle+=1
    if sickle>16:
        sickle-=17
        galeon+=1

print(f"Tenemos {knutsComienzo} knut. Cuanto será al cambio?")
print(f"Al cambio son {galeon} galeones, {sickle} sickle y {knut} knut.")



