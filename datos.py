import random


with open('Animales.txt', 'r') as archivo1:
    animal = archivo1.readlines()
    a = [linea.strip() for linea in animal]

archivo1.close()

with open('Colores.txt', 'r') as archivo2:
    color = archivo2.readlines()
    b = [linea.strip() for linea in color]

archivo2.close()



def generar_nombre():
    print(a.choise+b.choise)

def guardar_puntaje():
    pass

print(b)

#generar_nombre()