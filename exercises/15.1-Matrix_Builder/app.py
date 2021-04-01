import random

#Create the function below:
def matrixBuilder(num): 
    matriz = []
    arr1 = []

    #crea la matriz
    for inicializar in range(num):
        matriz.append([0]*num)

    for i in range(num): 
        for j in range(num):  
            matriz[i][j] = random.randint(1,1)
    return matriz


print(matrixBuilder(5))