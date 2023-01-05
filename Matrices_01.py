'''Suma, resta, multiplicación de matrices.'''

import numpy as np
Matriz_A=np.array([[2, 1, 1],[3, 1, 2],[1,-1, 0]])
Matriz_B=np.array([[1,-1, 3],[4, 3, 2],[1,-2, 5]])
print(f"""\tSean dos matrices cuadradas\n
Matriz A:\n 
{Matriz_A}\n
Matriz B:\n 
{Matriz_B}\n""")
print("Suma Matriz A + B:\n",Matriz_A+Matriz_B)
print("Resta Matriz A - B:\n",Matriz_A-Matriz_B)
print("Multiplicación de Matrz A * B:\n",Matriz_A*Matriz_B)
