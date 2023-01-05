'''Hallar la matriz simétrica'''
'''Sabemos que la una matriz es simétrica 
si la matriz es igual a su transpuesta'''

Matriz_A = [[2, 0, -1],[5, 1, 3],[-8, 2, 7]]
Matriz_B = [[5, 1, 3],[1, 8, 2],[3, 2, 5]]

def simetria_Matriz(matriz):
    if matriz == Transpuesta_Matriz(matriz):
        resultado=True
    else:
        resultado=False
    return resultado

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
        
def ejecucion_Matriz(matriz):
    imprimir_Matriz(matriz)
    A=simetria_Matriz(matriz)
    if A==True:
        print("La Matriz 'SI' es simetrico.")
    else:
        print("La matriz 'NO' es simetrico.")
    

print("Sea la Matriz A:")
ejecucion_Matriz(Matriz_A)

print("\nSea la Matriz B")
ejecucion_Matriz(Matriz_B)
