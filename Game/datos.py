import random
import json
import tkinter as tk
import tkinter.font as tkFont

ARCHIVO_PUNTAJES='puntaje.json'

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
            json.dump(mi_diccionario, archivo_json, indent=4)
    
    def mensaje():
        import json

        try:
            with open(ARCHIVO_PUNTAJES, 'r') as archivo_json2:
                tabla = json.load(archivo_json2)    
        except FileNotFoundError:
            tabla = {}

        sort_scores = dict(sorted(tabla.items(), key=lambda x: x[1], reverse=True))

        
       # mensaje_de_pantalla=tk.Label(root,text=sort_scores,padx=20,pady=10)
       # mensaje_de_pantalla.config(sort_scores)
       # mensaje_de_pantalla.grid(row=1,column=0,sticky="ew")
        string = 'Top 5: \n'
        veces = 1
        for k,v in sort_scores.items():
            string += f"{k}: {v}pts\n"
            veces+=1
            if veces == 5:
                break

        #print('Tendria que salir: \n',string)
        return str(string)

