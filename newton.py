import math

def funcao (x):
	return pow(x,3) - 9*x + 3

def derivada(x):
	return 3 * x **2 - 9

def newton(xo,limite):	
	f = funcao(xo)

	f_aux = f
	if(f_aux < 0): f_aux = f * - 1

	while(f_aux > limite):
		x = xo - (funcao(xo)/derivada(xo))

		f = funcao(x)
		f_aux = f
		if(f_aux < 0): f_aux = f * - 1
		xo = x
	
	return x