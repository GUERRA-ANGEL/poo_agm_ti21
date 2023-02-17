"""
    programa18.py
    nombre: Angel G.M.
    fecha: 09/02/2023
    descripcion: Forma 12
"""

def mayor(numero1:int,numero2:int)->int | None:  #Toma dos numeros enteros numero1 y numero2 al final de la definición de la función indica que la función puede devolver un entero o None
    result = None  #resultado es igual a None
    if numero1 > numero2:  #si numero1 es mayor
        result = numero1   #entonces el resultado es igual a numero1
    elif numero2 > numero1:  #sino numero2 es mayor numero1
        result = numero2 #entonces el resultado es numero2
    return result  #devuleve el resultado
 
print(mayor(2,1)) #2
print(mayor(1,2)) #2
print(mayor(2,2)) #None
print(mayor(2,-1)) #2
print(mayor(-1,2)) #2
print(mayor(-1,-1)) #None
print(mayor(-2,-1)) #-1
print(mayor(-1,-2)) #-1
