'''Crea dos arrays o arreglos unidimensionales que tengan
el mismo tamaño (lo pedirá por teclado), en uno de ellos
almacenarás nombres de personas como cadenas, en el
otro array o arreglo ira almacenando la longitud de los
nombres.'''

cantidad = int(input("Ingrese el tamaño de los arreglos: "))
Nombres = []
Tamaño_N = []
for i in range (1,cantidad+1):
    Nombres.append(str(input(f"Ingrese Nombre {i}: ")))
for j in range (cantidad):
 Tamaño_N.append(len(Nombres[j]))
print (Nombres) 
print (Tamaño_N)
