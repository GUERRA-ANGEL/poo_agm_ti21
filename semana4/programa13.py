"""
programa13.py
Nombre:Angel Guerra Muñoz
Fecha:07/02/2023
Descripcion:Crear programa de 2 numeros
"""

n1 = int(input("Numero1"))
n2 = int(input("Numero2"))

#Forma one
if n1>n2:
    print(n1)
if n2<n1:
    print(n2)
if n1==n2:
    print(None)
    
#Forma two
if n2>n1:
    print(n2)
if n1<n2:
    print(n1)
else:
    print(None) 
    
# Forma three     
if n1>n2:
    print(n1)
elif n2>n1:
    print(n2)
else:
    print(None)
    
# Forma four
if n1==n2:
    print(None)
elif n1>n2:
    print(n1)
elif n2>n1:
    print(n2)
    
# Forma five
if n1<n2:
    print(n2)
if n2<n1:
    print(n1)
if n1==n2:
    print(None)
    
# Forma six
if n2>n1:
    print(n2)
if n2<n1:
    print(n1)
else:
    print(None)
    
# Forma seven
if(n2<n1>n2):
    print(n1)
elif(n1<n2>n1):
    print(n2)
else:
    print(None)
    
# Forma eigth
if n1<=n2:
    print(n1)
if n1==n2:
    print(None)
else:
    print(n2)
