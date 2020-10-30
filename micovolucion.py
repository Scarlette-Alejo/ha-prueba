import numpy as np #<-- apodo

#Función que calcula la matriz resultante C después de aplicar la operación convolución de A*B
def convolucion(A,B):
    C = np.zeros((len(A)-2,len(A[0])-2))
    n = 0
    for i in range(len(C)):
        for j in range(len(C[0])):
            resultado = 0
            for iaux in range(len(B)):
                for jaux in range(len(B[0])):
                    resultado += A[i+iaux][j+jaux]*B[iaux][jaux]
            C[i][j] = resultado
    return C

matriz1 = [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro = [[1,0,2],[5,0,9],[6,2,1]]

A = np.array(matriz1)
B = np.array(filtro)

C = np.zeros((2,2))

#print(A)

#print(A[1,0])

x = convolucion(A,B)
print(x)

#C[0,0] = A[0,0]*B[0,0]+A[0,1]*B[0,1]+A[0,2]*B[0,2]+A[1,0]*B[1,0]+A[1,1]*B[1,1]+A[1,2]*B[1,2]+A[2,0]*B[2,0]+A[2,1]*B[2,1]+A[2,2]*B[2,2]
#C[0,1] = A[0,1]*B[0,0]+A[0,2]*B[0,1]+A[0,3]*B[0,2]+A[1,1]*B[1,0]+A[1,2]*B[1,1]+A[1,3]*B[1,2]+A[2,1]*B[2,0]+A[2,2]*B[2,1]+A[2,3]*B[2,2]

