"""
   programa24.py
   Nombre:Angel Guerra Muñoz
   Fecha:14/02/2023
   Descripcion:Realiza suma(otra forma)
""" 

numero1 = float(input("Ingrese numero: "))
numero2 = float(input("Ingrese numero: "))
def suma(numero1,numero2) -> float:
    if numero1>0:
        while numero1>0:
            numero2 +=1
            numero1 -=1
        return numero2
    else:
        while numero1<0:
            numero2 -=1
            numero1 +=1
        return numero2
    return suma(numero1,numero2)

resultado = suma(numero1,numero2 )
print(resultado)