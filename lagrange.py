import math

# Input
# y = [2.0,2.4,2.3,1.7,0.8]

# x = [1.5,2.5,4.0,5.5,7.0]

# x_find = 3

def lagrange (x,y,find):
    P = 0.0
    for j in range (len(x)):
        L_divisor = 0.0
        L_dividendo = 0.0
        L = 0.0
        for i in range(len(x)):  
            if i != j:
                if(L_dividendo == 0.0 and L_divisor == 0.0):
                    L_dividendo = (find - x[i])
                    L_divisor = (x[j] - x[i])
                else:
                    L_dividendo = L_dividendo * (find - x[i])
                    L_divisor = L_divisor * (x[j] - x[i])
            else:
                pass
            
        L = L_dividendo/L_divisor
        P = P + (y[j] * L)
    return round(P,2)






