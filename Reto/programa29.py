"""
   programa29.py
   Nombre:Angel Guerra Muñoz
   Fecha:19/02/2023
   Descripcion:Adivina el numero
""" 

num = int(input("Adivine el numero: "))
x = [1,10]

if num in x:
    print("Adivinaste")
else:
    print("No adivinaste")
    