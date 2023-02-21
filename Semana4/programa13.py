"""
programa13.py
Nombre:Angel Guerra Muñoz
Fecha:07/02/2023
Descripcion:Crear programa de 2 numeros
"""

n1 = int(input("Numero1: ")) #insertar numero 1
n2 = int(input("Numero2: ")) #insertar numero 2

#Forma 1
if n1>n2:  #si el numero1 es mayor que el numero2
    print(n1) #imprimir el numero1
if n2>n1:  #si el numero2 es mayor que el numero1
    print(n2) #imprimir el numero2
if n1==n2:  #si el numero1 es igual al numero2
    print(None)  #imprimir None
    
#Forma 2
if n2>n1:    #si el numero2 es mayor que el numero1
    print(n2)  #imprimir el numero2
if n1<n2:  #si el numero1 es menor que el numero2
    print(n1)  #imprimir el numero1
else:   #si no, es 
    print(None) #imprimir None
    
# Forma 3   
if n1>n2:    #si el numero1 es mayor que el numero2
    print(n1)  #imprimir el numero1
elif n2>n1:  #si el numero2 es mayor que el numero1
    print(n2)   #imprimir el numero2
else:       #sino ,es
    print(None)  #imprimir None
    
# Forma 4
if n1==n2:    #si el numero1 es igual al numero2
    print(None)   #imprimir None
elif n1>n2:    #si el numero1 es mayor que el numero2
    print(n1)   #imprimir el numero1
elif n2>n1:  #si el numero2 es mayor que el numero1
    print(n2)  #imprimir el numero2
    
# Forma 5
if n1<n2:   #si el numero1 es menor que el numero2
    print(n2)  #imprimir el numero2
if n2<n1:  #si el numero2 es menor que el numero1
    print(n1)  #imprimir el numero1
if n1==n2:   #si el numero1 es igual al numero2
    print(None)   #imprimir None
    
# Forma 6
if n2>n1:       #si el numero2 es mayor que el numero1
    print(n2)   #imprimir el numero2
if n2<n1:       #si el numero2 es menor que el numero1
    print(n1)   #imprimir el numero1
else:           #sino,es
    print(None) #imprimir None
    
# Forma 7
if(n2<n1>n2):  #si el numero2 es menor que el numero1 y el numero2 es mayor que el numero1
    print(n1)   #imprimir el numero1
elif(n1<n2>n1):  #si el numero1 es menor que el numero2 y el numero1 es mayor que el numero2
    print(n2)   #imprimir el numero2
else:    #si no, es
    print(None)  #imprimir None
    
# Forma 8
if n1<=n2:     #si el numero1 es menor o igual al numero2
    print(n1)  #imprimir el numero1
if n1==n2:     #si el numero1 es exactamente igual a numero2
    print(None) #imprimir None
else:           #sino,es 
    print(n2)  #imprimir el numero2

#Forma 9
def mayor(n1,n2):  #funcion que devuelve el mayor de los 2 numeros
    if n1>=n2:  #si el numero1 es mayor o igual al numero2
        if n1==n2: #si el numero1 es exactamente igual al numero2
            print(None)  #imprimir None
        else:         #sino,es
            print(n1)  #imprimir el numero1
    else:  #sino,es
      print(n2)     #impirmir el numero2 

mayor(n1,n2) #llama a la funcion mayor con numero1 y numero2

#Forma 10
if n2>=n1:              #si n2 es mayor o igual a n1
    if n2==n1:          #si n2 es exaxtamente igual a n1
        print(None)     #imprime None
    else:               #si no lo es
        print(n2)       #imprime n2
else:                   #sino
    print(n1)           #imprime n1
    
#Forma 11
if  n2 == n1 :
    print(None)
if n2 > n1:
    print(n2)
else:
    print(n1)
    