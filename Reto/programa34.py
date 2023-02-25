"""
   programa34.py
   Nombre:Angel Guerra Muñoz
   Fecha:24/02/2023
   Descripcion:Calcula la temperatura con los sonidos de un grillo
"""


num = float(input("Ingresa numero de sonidos por minuto de un grillo: "))

if num == 0:
    print("No se obtuvo ningún sonido")
    
else:
    temperatura = num / 4 + 40
    print("La temperatura en grado Farentheit es", temperatura)