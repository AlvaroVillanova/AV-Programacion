listaABC= "abcdefghijklmnopqrstuvwxyz"

def desplazarLetra(lista,palabra,numero):
    palabraCifrada=""
    for letra in palabra: 
        posLetra=listaABC.index(letra)
        nuevaPosLetra=(posLetra+numero)%len(lista)
        palabraCifrada+=listaABC[nuevaPosLetra]
    return palabraCifrada

fraseACifrar="perro"
palabraCifrada=""
numeroSecreto=3

palabraCifrada=desplazarLetra(listaABC,fraseACifrar,numeroSecreto)

print(fraseACifrar)
print(palabraCifrada)
