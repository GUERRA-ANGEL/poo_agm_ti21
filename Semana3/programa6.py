"""
   programa6
   Nombre:Angel Guerra Muñoz
   Fecha:/01/2023
   Descripcion:Crear una aplicación que permita calcular el área y perímetro de cualquier triangulo
""" 
lado1 = (input("lado1: "))
lado2 = (input("lado2: "))
lado3 = (input("lado3: "))
base = int(input("base: ")) #int sirve para agregar valores enteros
altura = int(input("altura: ")) # inputPara agregar una cantidad 

p = (lado1 + lado2 + lado3)
a = (base * altura)/2
print("El perimetro del triangulo es {} y el area del triangulo es: {}".format(p,a))
