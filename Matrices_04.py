'''Hallar la matriz transpuesta'''

Matriz = [[3, 8, -1],[9, 0, 2],[-5, 4, 5]]

def Transpuesta_Matriz(matriz):
    Transpuesta=[]
    for i in range (len(matriz[0])):
        Transpuesta.append([])
        for j in range (len(matriz)):
            Transpuesta[i].append(matriz[j][i])
    return Transpuesta

def imprimir_Matriz(matriz):
    for linea in matriz:
        for elemento in linea:
            print(elemento, end=" ")
        print()

Resultado = Transpuesta_Matriz(Matriz)
print("Sea la Matriz A:")
imprimir_Matriz(Matriz)

print("La transpuesta de la matriz A es:")
imprimir_Matriz(Resultado)
