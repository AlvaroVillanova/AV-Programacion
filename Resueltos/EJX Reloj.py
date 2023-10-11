#Hacer un reloj

import time

segundos=0
minutos=0
horas=0


# SOLUCION 1 (Hecha por Lupi)

for horas in range(1-11+1)
    for minutos in range(0,59+1)
        for segundos in range (0,59+1)
            time.sleep(1)
            print (f"{horas}:{minutos}.{segundos}")


# SOLUCION 2 (Hecha por mi)

while horas<24:
    time.sleep(1)
    segundos+=1
    if segundos>59:
        segundos=0
        minutos+=1
    if minutos>59:
        minutos=0
        horas+=1
    if horas>23:
        horas=0
    print(str(horas)+":"+str(minutos)+":"+str(segundos))

