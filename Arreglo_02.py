''' Dada las siguientes notas almacenadas en un arreglo:
[20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente sin usar la
función (min) y escriba en pantalla.
Luego programáticamente calcule el promedio de notas
descontando la nota eliminada.'''

Arreglo = [20, 15, 12, 11, 8, 4, 1]
maximo = 20
minimo = maximo
for i in Arreglo:
  if i<minimo:
    minimo=i
print ("Promedio más bajo es:",minimo)
Arreglo.remove(minimo)
print (Arreglo)
suma = 0
for j in Arreglo:
  suma+=j
print (suma)
print ("promedio de las notas es: ",suma/len(Arreglo))
