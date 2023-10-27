
"""
# Pirañas con sorpresa
Ayer lanzamos a un hombre a una piscina llena de pirañas y resulta que llevaba un anillo de oro que nadie le quitó antes de lanzarlo.
Hay entre 400 y 500 pirañas [Genera el valor aleatoriamente]

Sois 8 personas las que sabéis que una de las pirañas tiene el anillo de oro. Habéis decidido pescar las pirañas, comprobar si tienen el anillo por turnos, y volver a soltarlas inmediatamente después. ¿Quién encuentra el anillo? Explica cómo lo has implementado y por qué. 
```
Al pescar la piraña número 90: Petra se quedó con el añillo.
"""
import random

pescadores=["Pepito","Antoine","Cecil","Marietta"]
pescadorGanador=random.choice(pescadores)

minPiranas=400
maxPiranas=500
numPiranas=random.randrange(minPiranas,maxPiranas+1)

print(f"El numero de piranas es... {numPiranas}. ")

piranaGanadora= random.randrange(1,numPiranas)

print(f"Al pescar la pirania numero {piranaGanadora}: {pescadorGanador} se quedo con el anillo. ")

