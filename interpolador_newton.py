import math

def funcao(x,y,x1,y1):
    resultado = (y1 - y) / (x1 - x)
    return float(resultado)

def i_newton(x,y,find):   
    b = 0.0
    for i in range(len(x)):
        if i == 0:
            # f[x0]
            b = y[0]
            p = b
        if i == 1:
            b = funcao(x[i-1],y[i-1],x[i],y[i])
            p += b * (find - x[0])
        if (i != 0) and (i != 1):
            dividendo = 0.0
            for j in range(i):
                dividendo = dividendo - funcao(x[j],y[j],x[j+1],y[j+1])
            b = dividendo / (x[i] - x[0])
            for j in range(i):
                b *= find - x[j]
            p += b
        
    return p

        

