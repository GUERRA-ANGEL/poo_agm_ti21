minutos = int(input("Informe el tiempo en minutos: ")) # Se escribe el tiempo en minutos
distancia = int(input("Informe la distancia en metros: ")) #Se escribe la distancia en metros

seg = minutos/60 # Se divide los minutos por 60 para obtener los segundos
min = minutos # Se guarda el tiempo en minutos
horas = seg/60 # Se divide los segundos por 60 para obtener las horas
velocidad = distancia/seg # Se divide la distancia en segundos para obtener la velocidad

print("Tiempo en horas: ",horas)   # se imprime el tiempo en horas
print("Tiempo en segundos: ",min) # se imprime el tiempo en segundos
print("Tiempo en minutos: ",minutos)  # se imprime el tiempo en minutos
print("Distancia en metros: ",distancia) # se imprime la distancia en metros
print("Velocidad en metros/segundo: ",velocidad) # se imprime la velocidad en metros/segundos
