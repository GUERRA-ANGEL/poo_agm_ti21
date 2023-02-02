"""
   programa7
   Nombre:Angel Guerra Muñoz
   Fecha:31/01/2023
   Descripcion:Calcular el area y perimetro de circulo y cuadrado
"""   
lado1 = float(input("Coloca el lado1: ")) #El usuario colocara el lado1 del cuadrado
lado2 = float(input("Coloca el lado2: ")) #El usuario colocara el lado2 del cuadrado
lado3 = float(input("Coloca el lado3: ")) #El usuario colocara el lado3 del cuadrado
lado4 = float(input("Coloca el lado4: ")) #El usuario colocara el lado4 del cuadrado
a = lado1**2 #El area de un cuadrado de saca lado por lado o un lado al cuadrado
p = lado1 + lado2 + lado3 + lado4 #El perimetro de un cuadrado se aca sumando todos sus lados
print("El area del cuadrado es ={}".format(a)) #mandara a imprimir el area del cuadrado
print("El perimetro es ={}".format(p)) #mandara a imprimir el perimetro del cuadrado

Circulo = (input("Coloca los siguientes datos de un circulo")) #nombre de la figura geometrica
radio = float(input("Coloca el radio del circulo: ")) #El usuario colocara el o los numeros de la medida del radio
diametro = float(input("Coloca el diametro del circulo: ")) #El usuario colocara el o los numeros de la medida del diametro
PI = 3.141592 #Valor de PI
radio = diametro / 2
area = PI * radio **2
perimetro = 2 * PI * radio
print("El area del circulo es = {}".format(area)) #Mandara a imprimir el area del circulo
print("El perimetro del circulo es = {}".format(perimetro)) #Mandara a imprimir el perimetro del circulo
