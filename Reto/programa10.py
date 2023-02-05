"""
   programa10.py
   Nombre:Angel Guerra Muñoz
   Fecha:04/02/2023
   Descripcion:Calculadora de IMC
""" 

p = float(input("Inserte su peso en kilogramos: "))   #inserta el peso en kilogramos
a = float(input("Inserte su altura en metros: "))     #inserta la altura en metros

IMC = p/(a**2)    #calcula el IMC,es perimetro entre altura al cuadrado
print("Su IMC es = ",IMC)   #imprime el IMC

if IMC <=20 and IMC < 24.9:    #el rango de desnutricion en hombres es de 18.5kg a 25kg
    print("Tiene desnutricion en hombre")    #imprime desnutricion en hombre
elif IMC <=25 and IMC < 29.9:     #el rango de peso normal en hombres abarca de 25kg a 30kg
    print("Normal en hombre")   #imprime normal en hombre
elif IMC <=30 and IMC < 39.9:   #el rango de desnutricion en mujeres es de 39kg a 40kg
    print("obesidad en hombre")  #imprime obesidad en hombre
elif IMC <=40 and IMC > 1000: #el rango de desnutricion en mujeres abarca de 40kg a 50kg
    print("obesidad grave en hombre")   #imprime obesidad grave en hombre

if IMC <=20 and IMC <23.9:   #el rango de desnutricion en hombres es de 19kg a 24kg
    print("Tiene desnutricion en mujer")  #imorime desnutricion en mujer
elif IMC <=24 and IMC <28.9:   #el rango de peso normal en hombres abarca de 24kg a 27kg
    print("Normal en mujer")  #imprime el peso normal en mujer
elif IMC <=30 and IMC <40:   #el rango de desnutrici
    print("obesidad en mujer")   #imprime la obesidad en mujer
elif IMC >40:   #el rango de obesidad grave en mujer abarca de 32kg a 40kg
    print("obesidad grave en mujer")
