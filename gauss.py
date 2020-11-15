import math

def gauss (matriz):
    output = ""
    largura = len(matriz[0])
    for k in range(1,largura):
        nova = matriz
        if matriz[k-1][k-1] != 0:
            for i in range(k,len(matriz)):
                multplicador = int(matriz[i][k-1] / matriz[k-1][k-1])
                for j in range(k-1,largura):
                    aux = matriz[i][j] - multplicador * matriz[k-1][j]
                    nova[i][j] = aux
                    output += str(nova) + " \n"
        else:
            pass
    return output