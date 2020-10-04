import math

matriz = [
    [2,3,-1,5],
    [4,4,-3,3],
    [2,-3,1,-1]
]

def gauss (matriz):
    nova = matriz
    for i in range(1,len(matriz)):
        multplicador = int(matriz[i][0] / matriz[0][0])
        for j in range(len(matriz)):
            aux = matriz[i][j] - multplicador * matriz[i-1][j]
            nova[i][j] = aux
    

print(gauss(matriz))