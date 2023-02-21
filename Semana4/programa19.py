"""
    programa12.py
    nombre: Angel G.M.
    fecha: 09/02/2023
    descripcion: Bingo
"""
num = int(input("Ingresa numero: "))   #pide un numero
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]  #es el rango de numeros ganadores

if num in x:  #se utiliza para verificar si un valor num está presente en una lista x 
    print("bingo")  #imprime bingo
    