"""
    programa17.py
    nombre: Angel G.M.
    fecha: 09/02/2023
    descripcion: Forma 12
"""

def mayor(numero1,numero2): #definicion de mayor entre numero1 y numero2
    result =  None      #resultado None
    if numero1 > numero2:          #si numero1 es mayor que el numero2
        result = numero1           #El resultado es numero1
    elif numero2 > numero1:        #si numero2 es mayor que el numero1
        result = numero2           #El resultado es numero2

    return result                   #devuelve el valor resultado
print(mayor(2,1)) #2
print(mayor(1,2)) #2
print(mayor(2,2)) #None
print(mayor(2,-1)) #2
print(mayor(-1,2)) #2
print(mayor(-1,-1)) #None
print(mayor(-2,-1)) #-1
print(mayor(-1,-2)) #-1

