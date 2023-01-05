'''Multiplicación de matrices.'''

print("Ingresae el orden de su Matriz A")
Filas_1,Columnas_1 = int(input("Fila: ")),int(input("Columna: "))
print("Ingrese el orden de su Matriz B")
Filas_2,Columnas_2 = int(input("Fila: ")),int(input("Columna: "))

if Columnas_1==Filas_2:
	matriz_1 = []
	for i in range(Filas_1):
		matriz_1.append([0] * Columnas_1)
	matriz_2 = []
	for i in range(Filas_2):
		matriz_2.append([0] * Columnas_2)
	print("Ingrese su Matriz A")
	for i in range(Filas_1):
		for j in range(Columnas_1):
			matriz_1[i][j] = float(input("Elemento (%d,%d): " % (i, j)))
	print ("Ingrese su Matriz 2")
	for i in range(Filas_2):
		for j in range(Columnas_2):
			matriz_2[i][j] = float(input("Elemento (%d,%d): " % (i, j)))
	matriz_3 = []
	for i in range(Filas_1):
		matriz_3.append([0] * Columnas_2)
	for i in range(Filas_1):
		for j in range(Columnas_2):
			for k in range(Filas_2):
				matriz_3[i][j] += matriz_1[i][k] * matriz_2[k][j]
	print ("Su matriz resultante es:")
	print (matriz_3)
else:
	print ("Recuerde la multiplicacion entre matrices debe ser mxn * nxp")
