#Diseñe un algoritmo que permita ingresar la cantidad de escalas dentro de las cuales el turista debe ingresar la distancia a recorrer e ir sumando cada uno al final decir cuantas distancia y etapas realizar.
nombre = input("Ingrese nombre turista -> ")
etapas = int(input("Ingresar numero de etapas: -> "))
total_distancia = 0

for i in range(etapas):
    etapas_distancia = float(input(f"Ingrese la distancia de la etapa {i+1}: "))
    total_distancia += etapas_distancia

print(f"La distancia total de su viaje es {total_distancia}.")
print(f"Viajaras en estas {etapas} etapas.")
    
