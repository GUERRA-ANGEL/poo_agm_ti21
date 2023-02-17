"""
   programa26.py
   Nombre:Angel Guerra Muñoz
   Fecha:16/02/2023
   Descripcion:Piedra papel o tijeras
""" 

import random # se utiliza para generar la eleccion aleatoria de la computadora

opciones = ["piedra","papel","tijeras"]  #son las opciones que puede elegir el jugador piedra,papel o tijeras

while true:  #se ejecuta indefinidamente hasta que el jugador elige la opcion salir
    jugador =input("Elige piedra,papel o tijeras: ").lower() #elije pierda papel o tijeras, se utiliza para convertir la entrada del usuario en minúsculas y hacerla más fácil de comparar con las opciones válidas.

if jugador == "salir": #si el jugador coloca salir
    print("Hasta luego")  #Imprimira hasta luego
    break #Para cerrar el bucle
if jugador not in opciones:  #si el jugador escribe algo diferente
    print("opcion no valida,intentelo de nuevo.") #Imprimira opcion no valida intentalo de nuevo
    continue #Continua el programa

computadora = random.choice(opciones)  #La computadora eligira aleatoriamente entre las opciones piedra papel o tijeras
print("la computadora eligio:",computadora)  #Imprimira la computadora eligio

if jugador == computadora:  #si el jugador y la computadora eligen la misma opcion
    print("!Empate!") #Imprimira empate
elif jugador == "piedra" and computadora == "tijeras" or \ # Si el jugador elige piedra la computadora usara tijeras
     jugador == "papel" and compuradora == "piedra" or \ #si el jugador elige papel la computadora eligira pierda
     jugador == "tijeras" and computadora == "papel" or \ #si el jugador elije tijeras la computadora pondra papel"
     print("¡Ganaste!")  #imprimira ganaste
else:   #de lo contrario
     print("Perdiste!")  #imprimira perdiste
    