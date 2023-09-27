
def presentacion(name,edad):
    texto="Te llamas "+name+" y tienes "+edad+" anios de edad."
    return texto



name = input("Como te llamas?: ")
edad = input("Y tu edad?: ")
print(presentacion(name,edad))
