"""
   programa38.py
   Nombre:Angel Guerra Muñoz
   Fecha:28/02/2023
   Descripcion: Identifica si la palabra es palindroma
"""

miCadenaDeTexto = str(input("Ingrese una palabra: ")) #Sirve para ingresar y guardar una cadena de caracteres como es la palabra
if (miCadenaDeTexto) == (miCadenaDeTexto)[::-1]:    #e utiliza para crear una copia invertida de la cadena, [::-1] indica que se toma una porción de la cadena que comienza desde el final y se mueve hacia atrás en incrementos de uno.
    print("Es palindroma")  #Imprime "Es palindroma"
else:                       #Si no
    print("No es palindroma") #Imprime "No es palindroma"
