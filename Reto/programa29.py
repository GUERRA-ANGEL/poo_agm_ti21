"""
   programa29.py
   Nombre:Angel Guerra Muñoz
   Fecha:19/02/2023
   Descripcion:Adivina el numero
""" 

num = int(input("Adivine el numero: "))  #Inserta el numero para adivinar cual es
x = [1,10]  #Son los numeros ganadores

if num in x:                     #Se utiliza para verificar que el valor num si esta en la lista
    print("Adivinaste")    #Imprime Adivinaste
else:                      #Si no
    print("No adivinaste") #Imprime No adivinaste

    