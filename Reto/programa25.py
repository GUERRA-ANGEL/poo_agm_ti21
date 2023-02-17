"""
   programa24.py
   Nombre:Angel Guerra Muñoz
   Fecha:14/02/2023
   Descripcion:Realiza suma(otra forma)
""" 

numero1 = float(input("Ingrese numero: ")) #Inserar numero1
numero2 = float(input("Ingrese numero: "))  #Insertar numero2
def suma(numero1,numero2) -> float:  #definir suma de numero1 y numero2 flotante
    if numero1>0:           #Si 1 es mayor que 0
        while numero1>0:    #Bucle numero1 es mayor que 0
            numero2 +=1      #numero2 mas 1
            numero1 -=1      #numero1 menos 1
        return numero2       #regresa numero2
    else:                     #si no
        while numero1<0:      #Bucle de numero es menor que 0
            numero2 -=1       #numero2 menos 1
            numero1 +=1       #numero1 mas 1
        return numero2        #regresa numero2
    return suma(numero1,numero2)  #regresa la suma de numero1 mas el numero2

resultado = suma(numero1,numero2 )  #resultado es igual a suma de numero1 mas numero2
print(resultado)  #imprime resultado
