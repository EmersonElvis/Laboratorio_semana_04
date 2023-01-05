'''Calcular la determinante de una matriz'''
'''Para calcular el determinante de una matriz,
necesariamente el matriz tiene que ser 7
una matriz cuadrada.'''

import numpy as np

Matriz_A=np.array([[2, 1, 1],[3, 1, 2],[1,-1, 0]])
Matriz_B=np.array([[1,-1, 3],[4, 3, 2],[1,-2, 5]])

def determinante(m):
    print("Sea la matriz:\n",m)
    deter=np.linalg.det(m)
    print("El determinante es:\n",deter)
    
determinante(Matriz_A)
determinante(Matriz_B)
