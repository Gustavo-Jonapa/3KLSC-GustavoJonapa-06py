#Declaramos una lista de valores string
aves=["Loro gris ", "Paloma ", "Guacamaya "]
print('Los valores iniciales de la lista son: ')

#Iteramos sobre la lista para imprimir los valores 
for posicion in aves:
    print(posicion, end=" ")
    print("\n")

#Agregamos 3 elementos al final de la lista utilizando append()
aves.append("Zopilote ")
aves.append("Aguila ")
aves.append("Cuervo ")
print('Los valores finales de la lista son: ')

#Iteramos sobre la lista para imprimir los valores 
for posicion in aves:
    print(posicion, end=" ")
print("\n")
