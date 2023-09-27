"""
#Ejercicio 1: Es mayor de edad?

edad = int(input("Edad? "))
print("Es mayor de edad? ")
esMayorEdad = (edad>=18)

if esMayorEdad:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Ejercicio 2: Es fin de semana?


#Ejercicio 3: Es un número positivo?

num = int(input("Dame un número? "))
print("Es positivo? ")
esPositivo=(num > 0)
if esPositivo:
    print("Si, es positivo ")
elif num==0:
    print("Es cero ")
else:
    print("No, es negativo ")
 

#Ejercicio 4: Es una vocal?

"""

#Ejercicio 5: Has aprobado el examen?

nota=float(input("Que nota has sacado? "))
print("Tu resultado es... ")
if nota<0 or nota>10:
    print("El número introducido es incorrecto. Inténtalo de nuevo. ")
elif nota>=0 and nota<5:
    print("Estas suspenso ")
elif nota<6:
    print("Has sacado un suficiente. ")
elif nota<7:
    print("Has sacado un bien. ")
elif nota<9:
    print("Has sacado un notable. ")
else:
    print("Enhorabuena, tienes un sobresaliente. ")





"""    
Clase y apuntes

Usar esto para revisar tipo de data type  ->  print(type(esMayorEdad))
"""
   
