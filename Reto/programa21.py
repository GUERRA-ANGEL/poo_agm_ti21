"""
   programa21.py
   Nombre:Angel Guerra Muñoz
   Fecha:11/02/2023
   Descripcion:Calcular el area y perimetro del rombo
"""  

d1 = float(input("Ingrese la medida de uno de los diagonales (en centímetros): ")) # Ingresa el valor de la medida de uno de los diagonales en centimetros del rombo
d2 = float(input("Ingrese la medida de la otra diagonal (en centímetros): "))  # Ingresa el valor de la medida de la otra diagonal en centimetros del rombo

def perimetro(d1, d2):   # Funcion que calcula el perimetro del rombo
    return 2 * (d1 + d2) # Hace la operacion de d1 + d2 y luego lo multiplica por 2 

def area(d1, d2):    # Funcion que calcula el area del rombo
    return (d1 * d2) / 2  # Hace la operacion de d1 * d2 y luego lo divide por 2

    
print("El perimetro del rombo es: ", perimetro(d1, d2))  # Imprime el resultado de la funcion
print("El área del rombo es: ", area(d1, d2))   # Imprime el resultado de la funcion
