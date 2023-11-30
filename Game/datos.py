import random
import json

ARCHIVO_PUNTAJES='puntaje.json'
MENSAJE='mensaje.json'

class PlayerName():
    
    def generar_nombre():
        with open('Animales.txt', 'r') as archivo1:
            animal = archivo1.readlines()
            a = [linea.strip() for linea in animal]
    
        with open('Colores.txt', 'r') as archivo2:
            color = archivo2.readlines()
            b = [linea.strip() for linea in color]

        nombre = random.choice(a)+' '+random.choice(b)
        
        return nombre

    def guardar_puntaje(nombre, puntaje):
        import json

        try:
        # Abrir el archivo JSON y cargar el diccionario
            with open(ARCHIVO_PUNTAJES, 'r') as archivo_json:
                mi_diccionario = json.load(archivo_json)    
        except FileNotFoundError:
            mi_diccionario = {}

        # Agregar elementos al diccionario
        mi_diccionario[nombre] = puntaje

        # Guardar los cambios en el archivo JSON
        with open(ARCHIVO_PUNTAJES, 'w') as archivo_json:
            json.dump(mi_diccionario, archivo_json)
    """
    def mensaje():
        import json

        try:
        # Abrir el archivo JSON y cargar el diccionario
            with open(MENSAJE, 'r') as archivo_json2:
                tabla = json.load(archivo_json2)    
        except FileNotFoundError:
            tabla = {}

        # Agregar elementos al diccionario
        mi_diccionario[nombre] = puntaje

        # Guardar los cambios en el archivo JSON
        with open(MENSAJE, 'w') as archivo_json2:
            json.dump(tabla, archivo_json2) 
        
        #print(f'Nombre : {nombre} | {puntaje}pts.')
    """