"""
    programa17.py
    nombre: Angel G.M.
    fecha: 09/02/2023
    descripcion: Determina la edad child,teen,adult.
"""

age = int(input("Escriba su edad; "))  # Se inscribe el valor de edad
if age>0 and age<=11: # Se comprueba que la edad sea entre 0 y 11
  print ("child")  # Se imprime el mensaje "child"
elif age>=12 and age<=17: # Se comprueba que la edad sea entre 12 y 17
    print("Teen")  # Se imprime el mensaje "teen"
elif age>=18 and age<=64:  # Se comprueba que la edad sea entre 18 y 64
    print("Adult") # Se imprime el mensaje "adult"