import random

archivo1=open('Animales.txt', 'r')
a=[archivo1.readline()]
archivo1.close()
archivo2=open('Colores.txt', 'r')
b=[archivo2.readline()]
archivo2.close()

def generar_nombre():
    print(a.choise+b.choise)

def guardar_puntaje():
    pass

generar_nombre()