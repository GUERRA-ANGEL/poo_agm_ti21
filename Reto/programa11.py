nom = (input("Escribe tu nombre: "))
edad = int(input("Escribe tu edad: "))
if edad < 18:
    print("joven")
if edad <= 18:
    print("Adulto")
if edad > 18 and edad < 60:
    print("Adulto")
if edad > 60 and edad < 1000:
    print("Anciano")
    