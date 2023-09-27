#Vamos a crear una funcion que alimentaremos con tres números y nos dará la media


#Funciones.

#num1,num2,num3 son argumentos de entrada y el resultado es el argumento de salida.

def otraMediaTresNumeros(num1,num2,num3):
        return (num1+num2+num3)/3

def mediaTresNumeros(num1,num2,num3):
        resultado=(num1+num2+num3)/3
        return resultado

    

#Podemos tener funciones sin return.
#Esto es una excepcion, de normal no usamos print() en funciones, solo cuando el objetivo de la funcion sea mostrar algo.

def crearLinea(forma):
    return(forma*30)

#Main
"""
print("Probando... ")
resultado1, resultado2, resultado3 = float (input("dame tus medias"))
media = mediaTresNumeros(resultado1, resultado2, resultado3)
print(media)

"""

a=69
b=420
c=666
media=otraMediaTresNumeros(a,b,c)

print(crearLinea("o"))
#print("La media de " + str(a) + ", " + str(b) + " y " + str(c) + " es: " + str(otraMediaTresNumeros(a,b,c)) + ".")
print(f"La media de {a}, {b} y {c} es {media}")
print(crearLinea("O"))
