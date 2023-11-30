import random


with open('Animales.txt', 'r') as archivo1:
    animal = archivo1.readlines()
    a = [linea.strip() for linea in animal]
archivo1.close()
with open('Colores.txt', 'r') as archivo2:
    color = archivo2.readlines()
    b = [linea.strip() for linea in color]
archivo2.close()


class Player():
    def __init__(self):
        self.nombre=''
        self.puntaje=0

    def generar_nombre(self,nombre):
        nombre = random.choice(a)+' '+random.choice(b)
        return nombre

    def guardar_puntaje(self,puntaje):
        pass

    def mensaje():
        pass

