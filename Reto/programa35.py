"""
   programa35.py
   Nombre:Angel Guerra Muñoz
   Fecha:25/02/2023
   Descripcion:Coloca los numeros colocados en forma descentente
"""

Num1 = float(input("Ingrese el numero: "))  #Ingresa numero
Num2 = float(input("Ingrese el numero: "))  #Ingresa numero
Num3 = float(input("Ingrese el numero: "))  #Ingresa numero

if Num1>Num2>Num3:               #Si numero1 es mayor que numero2 y numero2 es mayor que numero3
    print(Num1,Num2,Num3)        #Imprimir numero1.numero2,numero3
if Num3>Num2>Num1:               #Si numero3 es mayor que numero2 y numero2 es mayor que numero1
    print(Num3,Num2,Num1)        #Imprimir numero3.numero2,numero1
if Num2<Num3<Num1:               #Si numero2 es mayor que numero3 y numero3 es mayor que numero1
    print(Num2,Num3,Num1)        #imprimir numero2,numero3,numero1