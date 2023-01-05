'''Calcular la diagonal principal de una matriz'''
#Para cualcular el diagonal principal de una matriz
#Necesariamente la matriz tiene que ser cuadrada

print("Ingresae el orden de su Matriz A")
Fila = int(input("Fila: "))
Columna = int(input("Columna: "))

diagonal = 0

if Fila == Columna:
    matriz = []
    for i in range(Fila):
        matriz.append([0] * Columna)
    
    print("Ingrese su Matriz A")
    for i in range(Fila):
        for j in range(Columna):
            matriz[i][j] = float(input(f"Ingrese la posicion número {i},{j}: "))
    for i in range(Fila):
        for j in range(Columna):
            if i == j:
                diagonal += matriz[i][j]
    print("El valor de la diagonal prinicipal es:", diagonal)
else:
    print("Recuerde que la matriz tiene que ser cuadrada")
