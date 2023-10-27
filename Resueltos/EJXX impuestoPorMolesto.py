#ENUNCIADO: Impuesto por molesto

"""
Los fantasmas son seres molestos principalmente por el hecho de que se encargan de transmitir su aburrida existencia a toda persona que se acerque a ellos, por eso han decidido ponerles un impuesto que consiste en quitarle de su paga fantasmal un 2% por cada siglo de vida. 
[Crea una función a la que le pases la edad y el sueldo del fantasma y te devuelva cuánto tiene que pagar por plasta.]
```
¿Cuántos años tiene el fantasma? 465
¿Cuánto dinero gana? 10.010
Debe pagar un 8% -> 800,8€ 

"""
#FUNCIONES

def calculoPago(edadFantasma,sueldoFantasma,interesPorSiglo):
    porcentajeTotalAPagar=(edadFantasma//plazoPagoAnios)*interesPorSiglo
    debePagar=(sueldoFantasma*interesPorSiglo)/100
    return debePagar

#VARIABLES

edadFantasma=465 #int(input("Que edad tiene el fantasma? "))
sueldoFantasma=10010 #int(input("Cuanto gana el fantasma? "))
plazoPagoAnios=100
interesPorSiglo=2 #int(input("Que porcentaje por siglo es deducido de su sueldo? "))


#CUERPO

debePagar=calculoPago(edadFantasma,sueldoFantasma,interesPorSiglo)
print(f"Este fantasma debe pagar un {interesPorSiglo}% de su sueldo de {sueldoFantasma} euros por siglo: Paga {debePagar} euros.")