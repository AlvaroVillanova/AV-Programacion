"""

Eres un vampiro con más de 1000 años pero una despensa de tamaño limitado compuesta por botes 
de 3 y 5 litros.
Necesitas mantener al día tus depósitos de sangre y para eso llevas un control exhaustivo de 
los botes que tienes vacíos de cada tipo de cada tipo.
¿Lo malo? Que cuando vas a robar sangre solo puedes hacerlo en garrafas de 7 litros...

Crea un programa que solicite el número de botes que tienes vacíos y cuántas garrafas has comprado
y una función que devuelva True o False dependiendo de si te has pasado o no comprando garrafas.

Empezando a rellenar por los botes de 5 litros debes calcular: 
- Si no te has pasado comprando: 
    - ¿Cuántos botes de 5 litros (de los que tenías vacíos has rellenado)?
    - ¿Cuántos botes de 3 litros (de los que tenías vacíos has rellenado)?
    - Si algún bote se ha quedado a medias, cuántos litros le faltan.
- Si te has pasado comprando:
    - ¿Cuántos litros han sobrado?

[NOTA: Para hacer una división exacta (quedándonos solo con el cociente) se usa // en vez de /]

"""

#Solicitamos botes almacenados y garrafas compradas

botes3L=int(input("Cuantos botes vacios de 3L tienes en tu despensa? "))
botes5L=int(input("Y cuantos botes de 5L? "))
garrafasCompradas=int(input("Cuantas garrafas de 7 litros quieres comprar? "))


#Convertimos a litros totales capacidad/comprados. Boolean de pasarse

capacidadLitros = (botes3L*3)+(botes5L*5)
litrosComprados = garrafasCompradas*7
tePasasteGarrafas = litrosComprados > capacidadLitros
print(f"Te pasaste comprando garrafas?: {tePasasteGarrafas}")
    

#

if tePasasteGarrafas:
    print(f"Te has pasado comprando sangre: has llenado todos tus botes y aun te sobran {litrosComprados-capacidadLitros} litros en tus garrafas.  ")
else:

    botes5Llenos=capacidadLitros//(botes5L*5)
    capacidadLitros=capacidadLitros%(botes5L*5)
    print(f"Has llenado {botes5Llenos} de los botes de 5 litros que tenias. ")

    botes3Llenos=capacidadLitros//(botes3L*3)
    capacidadLitros=capacidadLitros%(botes3L*3)
    print(f"Has llenado {botes3Llenos} de los botes de 3 litros que tenias. ")

if capacidadLitros==0:
    print("Wuau! Has comprado la cantidad exacta de sangre para todos tus botes! ")
else:
    print(f"Vaya, parece que aun podrias haber almacenado {capacidadLitros} litros mas en un bote")

5