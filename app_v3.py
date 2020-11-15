import tkinter as tk
import tkinter.font as tkFont
import math
import bissecao as bissecao
import newton as newton
import gauss as gauss
import lagrange as lagrange
import interpolador_newton as i_newton

root = tk.Tk()
root.geometry("700x700")
root.title("Calculadora")

def bt_Bissecaao():
    biss_a_label.grid()
    biss_a_value.grid()
    biss_b_label.grid()
    biss_b_value.grid()
    biss_emp.grid()
    biss_epslon.grid()
    biss_epslon_value.grid()
    biss_result.grid()
    biss_bt.grid()
    
    new_bt.grid_remove()
    new_chute_label.grid_remove()
    new_chute_value.grid_remove()
    new_emp.grid_remove()
    new_epslon.grid_remove()
    new_epslon_entry.grid_remove()
    new_result.grid_remove()

    gau_bt.grid_remove()
    gau_emp.grid_remove()
    gau_expr1_label.grid_remove()
    gau_expr1_value.grid_remove()
    gau_expr2_label.grid_remove()
    gau_expr2_value.grid_remove()
    gau_expr3_label.grid_remove()
    gau_expr3_value.grid_remove()

    lag_bt.grid_remove()
    lag_emp.grid_remove()
    lag_expr1_label.grid_remove()
    lag_expr1_value.grid_remove()
    lag_expr2_label.grid_remove()
    lag_expr2_value.grid_remove()
    lag_expr3_label.grid_remove()
    lag_expr3_value.grid_remove()
    lag_result.grid_remove()

    inew_bt.grid_remove()
    inew_emp.grid_remove()
    inew_expr1_label.grid_remove()
    inew_expr1_value.grid_remove()
    inew_expr2_label.grid_remove()
    inew_expr2_value.grid_remove()
    inew_expr3_label.grid_remove()
    inew_expr3_value.grid_remove()
    inew_result.grid_remove()

def bt_Newton():
    new_bt.grid()
    new_chute_label.grid()
    new_chute_value.grid()
    new_emp.grid()
    new_epslon.grid()
    new_epslon_entry.grid()
    new_result.grid()

    biss_a_label.grid_remove()
    biss_a_value.grid_remove()
    biss_b_label.grid_remove()
    biss_b_value.grid_remove()
    biss_emp.grid_remove()
    biss_epslon.grid_remove()
    biss_epslon_value.grid_remove()
    biss_result.grid_remove()
    biss_bt.grid_remove()

    gau_bt.grid_remove()
    gau_emp.grid_remove()
    gau_expr1_label.grid_remove()
    gau_expr1_value.grid_remove()
    gau_expr2_label.grid_remove()
    gau_expr2_value.grid_remove()
    gau_expr3_label.grid_remove()
    gau_expr3_value.grid_remove()
    gau_result.grid_remove()

    lag_bt.grid_remove()
    lag_emp.grid_remove()
    lag_expr1_label.grid_remove()
    lag_expr1_value.grid_remove()
    lag_expr2_label.grid_remove()
    lag_expr2_value.grid_remove()
    lag_expr3_label.grid_remove()
    lag_expr3_value.grid_remove()
    lag_result.grid_remove()

    inew_bt.grid_remove()
    inew_emp.grid_remove()
    inew_expr1_label.grid_remove()
    inew_expr1_value.grid_remove()
    inew_expr2_label.grid_remove()
    inew_expr2_value.grid_remove()
    inew_expr3_label.grid_remove()
    inew_expr3_value.grid_remove()
    inew_result.grid_remove()

def bt_Gauss():
    gau_bt.grid()
    gau_emp.grid()
    gau_expr1_label.grid()
    gau_expr1_value.grid()
    gau_expr2_label.grid()
    gau_expr2_value.grid()
    gau_expr3_label.grid()
    gau_expr3_value.grid()

    new_bt.grid_remove()
    new_chute_label.grid_remove()
    new_chute_value.grid_remove()
    new_emp.grid_remove()
    new_epslon.grid_remove()
    new_epslon_entry.grid_remove()
    new_result.grid_remove()

    biss_a_label.grid_remove()
    biss_a_value.grid_remove()
    biss_b_label.grid_remove()
    biss_b_value.grid_remove()
    biss_emp.grid_remove()
    biss_epslon.grid_remove()
    biss_epslon_value.grid_remove()
    biss_result.grid_remove()
    biss_bt.grid_remove()

    lag_bt.grid_remove()
    lag_emp.grid_remove()
    lag_expr1_label.grid_remove()
    lag_expr1_value.grid_remove()
    lag_expr2_label.grid_remove()
    lag_expr2_value.grid_remove()
    lag_expr3_label.grid_remove()
    lag_expr3_value.grid_remove()
    lag_result.grid_remove()

    inew_bt.grid_remove()
    inew_emp.grid_remove()
    inew_expr1_label.grid_remove()
    inew_expr1_value.grid_remove()
    inew_expr2_label.grid_remove()
    inew_expr2_value.grid_remove()
    inew_expr3_label.grid_remove()
    inew_expr3_value.grid_remove()
    inew_result.grid_remove()

def bt_LU():
    new_bt.grid_remove()
    new_chute_label.grid_remove()
    new_chute_value.grid_remove()
    new_emp.grid_remove()
    new_epslon.grid_remove()
    new_epslon_entry.grid_remove()
    new_result.grid_remove()

    gau_bt.grid_remove()
    gau_emp.grid_remove()
    gau_expr1_label.grid_remove()
    gau_expr1_value.grid_remove()
    gau_expr2_label.grid_remove()
    gau_expr2_value.grid_remove()
    gau_expr3_label.grid_remove()
    gau_expr3_value.grid_remove()
    gau_result.grid_remove()

    biss_a_label.grid_remove()
    biss_a_value.grid_remove()
    biss_b_label.grid_remove()
    biss_b_value.grid_remove()
    biss_emp.grid_remove()
    biss_epslon.grid_remove()
    biss_epslon_value.grid_remove()
    biss_result.grid_remove()
    biss_bt.grid_remove()

    lag_bt.grid_remove()
    lag_emp.grid_remove()
    lag_expr1_label.grid_remove()
    lag_expr1_value.grid_remove()
    lag_expr2_label.grid_remove()
    lag_expr2_value.grid_remove()
    lag_expr3_label.grid_remove()
    lag_expr3_value.grid_remove()
    lag_result.grid_remove()

    inew_bt.grid_remove()
    inew_emp.grid_remove()
    inew_expr1_label.grid_remove()
    inew_expr1_value.grid_remove()
    inew_expr2_label.grid_remove()
    inew_expr2_value.grid_remove()
    inew_expr3_label.grid_remove()
    inew_expr3_value.grid_remove()
    inew_result.grid_remove()

def bt_Interpolador_Newton():
    inew_bt.grid()
    inew_emp.grid()
    inew_expr1_label.grid()
    inew_expr1_value.grid()
    inew_expr2_label.grid()
    inew_expr2_value.grid()
    inew_expr3_label.grid()
    inew_expr3_value.grid()
    inew_result.grid()

    new_bt.grid_remove()
    new_chute_label.grid_remove()
    new_chute_value.grid_remove()
    new_emp.grid_remove()
    new_epslon.grid_remove()
    new_epslon_entry.grid_remove()
    new_result.grid_remove()

    gau_bt.grid_remove()
    gau_emp.grid_remove()
    gau_expr1_label.grid_remove()
    gau_expr1_value.grid_remove()
    gau_expr2_label.grid_remove()
    gau_expr2_value.grid_remove()
    gau_expr3_label.grid_remove()
    gau_expr3_value.grid_remove()
    gau_result.grid_remove()

    biss_a_label.grid_remove()
    biss_a_value.grid_remove()
    biss_b_label.grid_remove()
    biss_b_value.grid_remove()
    biss_emp.grid_remove()
    biss_epslon.grid_remove()
    biss_epslon_value.grid_remove()
    biss_result.grid_remove()
    biss_bt.grid_remove()

    lag_bt.grid_remove()
    lag_emp.grid_remove()
    lag_expr1_label.grid_remove()
    lag_expr1_value.grid_remove()
    lag_expr2_label.grid_remove()
    lag_expr2_value.grid_remove()
    lag_expr3_label.grid_remove()
    lag_expr3_value.grid_remove()
    lag_result.grid_remove()

def bt_Interpolador_Lagrange():
    lag_bt.grid()
    lag_emp.grid()
    lag_expr1_label.grid()
    lag_expr1_value.grid()
    lag_expr2_label.grid()
    lag_expr2_value.grid()
    lag_expr3_label.grid()
    lag_expr3_value.grid()
    lag_result.grid()

    new_bt.grid_remove()
    new_chute_label.grid_remove()
    new_chute_value.grid_remove()
    new_emp.grid_remove()
    new_epslon.grid_remove()
    new_epslon_entry.grid_remove()
    new_result.grid_remove()

    gau_bt.grid_remove()
    gau_emp.grid_remove()
    gau_expr1_label.grid_remove()
    gau_expr1_value.grid_remove()
    gau_expr2_label.grid_remove()
    gau_expr2_value.grid_remove()
    gau_expr3_label.grid_remove()
    gau_expr3_value.grid_remove()
    gau_result.grid_remove()

    biss_a_label.grid_remove()
    biss_a_value.grid_remove()
    biss_b_label.grid_remove()
    biss_b_value.grid_remove()
    biss_emp.grid_remove()
    biss_epslon.grid_remove()
    biss_epslon_value.grid_remove()
    biss_result.grid_remove()
    biss_bt.grid_remove()

    inew_bt.grid_remove()
    inew_emp.grid_remove()
    inew_expr1_label.grid_remove()
    inew_expr1_value.grid_remove()
    inew_expr2_label.grid_remove()
    inew_expr2_value.grid_remove()
    inew_expr3_label.grid_remove()
    inew_expr3_value.grid_remove()
    inew_result.grid_remove()


def conta_bissecaao():
    n = float(biss_a_value.get())
    x = float(biss_b_value.get())
    eps = float(biss_epslon_value.get())
    result = float(bissecao.bisseccao(n,x,eps))
    biss_result.delete(0,'end')
    biss_result.insert(0,result)

def conta_newton():
    entry1 = float(new_chute_value.get())
    entry2 = float(new_epslon_entry.get())
    result = float(newton.newton(entry1,entry2))
    new_result.delete(0,'end')
    new_result.insert(0,result)

def conta_gauss():
    entry1 = list(gau_expr1_value.get().split(","))
    entry1 = [int(x) for x in entry1]
    entry2 = list(gau_expr2_value.get().split(","))
    entry2 = [int(x) for x in entry2]
    entry3 = list(gau_expr3_value.get().split(","))
    entry3 = [int(x) for x in entry3]
    listA = []
    listA.append(entry1)
    listA.append(entry2)
    listA.append(entry3)

    result = str(gauss.gauss(listA))
    gau_result = tk.Label(root,text = result)
    gau_result.grid(row=7, column = 1)

def conta_iLagrange():
    entry1 = list(lag_expr1_value.get().split(","))
    entry1 = [float(x) for x in entry1]
    entry2 = list(lag_expr2_value.get().split(","))
    entry2 = [float(x) for x in entry2]
    entry3 = float(lag_expr3_value.get())

    result = float(lagrange.lagrange(entry1,entry2,entry3))
    lag_result.delete(0,'end')
    lag_result.insert(0,result)

def conta_iNewton():
    entry1 = list(inew_expr1_value.get().split(","))
    entry1 = [float(x) for x in entry1]
    entry2 = list(inew_expr2_value.get().split(","))
    entry2 = [float(x) for x in entry2]
    entry3 = float(inew_expr3_value.get())

    result = float(i_newton.i_newton(entry1,entry2,entry3))
    inew_result.delete(0,'end')
    inew_result.insert(0,result)
    

# Fontes
fontStyle1 = tkFont.Font(family="Times", size=20)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=13)

##############################################################################

biss_subtitle = tk.Button(root, text="Método da Bissecção",font = fontStyle2, command = bt_Bissecaao, width = 20)
biss_subtitle.grid(row=0, column = 0)

new_subtitle = tk.Button(root, text="Método de Newton", font = fontStyle2, command = bt_Newton, width = 20)
new_subtitle.grid(row=0, column = 1)

gauss_subtitle = tk.Button(root, text="Método de Gauss", font = fontStyle2, command = bt_Gauss, width = 20)
gauss_subtitle.grid(row=1, column = 0)

lu_subtitle = tk.Button(root, text="Método de LU", font = fontStyle2, command = bt_LU, width = 20)
lu_subtitle.grid(row=1, column = 1)

lag_subtitle = tk.Button(root, text="Interpolador de Newton", font = fontStyle2, command = bt_Interpolador_Newton, width = 20)
lag_subtitle.grid(row=0, column = 2)

iNew_subtitle = tk.Button(root, text="Interpolador de Lagrange", font = fontStyle2, command = bt_Interpolador_Lagrange, width = 20)
iNew_subtitle.grid(row=1, column = 2)

##############################################################################

biss_emp = tk.Label(root, text="")
biss_emp.grid(row=2, column = 0)
biss_emp.grid_remove()

biss_a_label = tk.Label(root, text = "a = ")
biss_a_label.grid(row=3, column = 0)
biss_a_label.grid_remove()

biss_a_value = tk.Entry(root, font=fontStyle1)
biss_a_value.grid(row=3, column = 1)
biss_a_value.grid_remove()

biss_b_label = tk.Label(root, text = "b = ")
biss_b_label.grid(row=4, column = 0)
biss_b_label.grid_remove()

biss_b_value = tk.Entry(root, font=fontStyle1)
biss_b_value.grid(row=4, column = 1)
biss_b_value.grid_remove()

biss_epslon = tk.Label(root, text = "Epslon = ")
biss_epslon.grid(row=5, column = 0)
biss_epslon.grid_remove()

biss_epslon_value = tk.Entry(root, font=fontStyle1)
biss_epslon_value.grid(row=5, column = 1)
biss_epslon_value.grid_remove()

biss_bt = tk.Button(root, text = "=", command = conta_bissecaao)
biss_bt.grid(row=6, column = 1)
biss_bt.config(height = 2, width = 5)
biss_bt.grid_remove()

biss_result = tk.Entry(root,font = fontStyle1)
biss_result.grid(row=7, column = 1)
biss_result.grid_remove()

##############################################################################

new_emp = tk.Label(root, text="")
new_emp.grid(row=2, column = 0)
new_emp.grid_remove()

new_chute_label = tk.Label(root, text = "Chute = ")
new_chute_label.grid(row=3, column = 0)
new_chute_label.grid_remove()

new_chute_value = tk.Entry(root, font=fontStyle1)
new_chute_value.grid(row=3, column = 1)
new_chute_value.grid_remove()

new_epslon = tk.Label(root, text = "Epslon = ")
new_epslon.grid(row=4, column = 0)
new_epslon.grid_remove()

new_epslon_entry = tk.Entry(root, font=fontStyle1)
new_epslon_entry.grid(row=4, column = 1)
new_epslon_entry.grid_remove()

new_bt = tk.Button(root, text = "=", command = conta_newton)
new_bt.grid(row=5, column = 1)
new_bt.config(height = 2, width = 5)
new_bt.grid_remove()

new_result = tk.Entry(root,font = fontStyle1)
new_result.grid(row=6, column = 1)
new_result.grid_remove()

##############################################################################

gau_emp = tk.Label(root, text="")
gau_emp.grid(row=2, column = 0)
gau_emp.grid_remove()

gau_expr1_label = tk.Label(root, text = "Elemento = ")
gau_expr1_label.grid(row=3, column = 0)
gau_expr1_label.grid_remove()

gau_expr1_value = tk.Entry(root, font=fontStyle1)
gau_expr1_value.grid(row=3, column = 1)
gau_expr1_value.grid_remove()

gau_expr2_label = tk.Label(root, text = "Elemento = ")
gau_expr2_label.grid(row=4, column = 0)
gau_expr2_label.grid_remove()

gau_expr2_value = tk.Entry(root, font=fontStyle1)
gau_expr2_value.grid(row=4, column = 1)
gau_expr2_value.grid_remove()

gau_expr3_label = tk.Label(root, text = "Elemento = ")
gau_expr3_label.grid(row=5, column = 0)
gau_expr3_label.grid_remove()

gau_expr3_value = tk.Entry(root, font=fontStyle1)
gau_expr3_value.grid(row=5, column = 1)
gau_expr3_value.grid_remove()

gau_bt = tk.Button(root, text = "=", command = conta_gauss)
gau_bt.grid(row=6, column = 1)
gau_bt.config(height = 2, width = 5)
gau_bt.grid_remove()

gau_result = tk.Label(root, text = "", font = fontStyle1)
gau_result.grid(row = 7, column = 1)
gau_result.grid_remove()

##############################################################################

lag_emp = tk.Label(root, text="")
lag_emp.grid(row=2, column = 0)
lag_emp.grid_remove()

lag_expr1_label = tk.Label(root, text = "Lista X = ")
lag_expr1_label.grid(row=3, column = 0)
lag_expr1_label.grid_remove()

lag_expr1_value = tk.Entry(root, font=fontStyle1)
lag_expr1_value.grid(row=3, column = 1)
lag_expr1_value.grid_remove()

lag_expr2_label = tk.Label(root, text = "Lista Y = ")
lag_expr2_label.grid(row=4, column = 0)
lag_expr2_label.grid_remove()

lag_expr2_value = tk.Entry(root, font=fontStyle1)
lag_expr2_value.grid(row=4, column = 1)
lag_expr2_value.grid_remove()

lag_expr3_label = tk.Label(root, text = "Encontrar X = ")
lag_expr3_label.grid(row=5, column = 0)
lag_expr3_label.grid_remove()

lag_expr3_value = tk.Entry(root, font=fontStyle1)
lag_expr3_value.grid(row=5, column = 1)
lag_expr3_value.grid_remove()

lag_bt = tk.Button(root, text = "=", command = conta_iLagrange)
lag_bt.grid(row=6, column = 1)
lag_bt.config(height = 2, width = 5)
lag_bt.grid_remove()

lag_result = tk.Entry(root,font = fontStyle1)
lag_result.grid(row=7, column = 1)
lag_result.grid_remove()

##############################################################################

inew_emp = tk.Label(root, text="")
inew_emp.grid(row=2, column = 0)
inew_emp.grid_remove()

inew_expr1_label = tk.Label(root, text = "Lista X = ")
inew_expr1_label.grid(row=3, column = 0)
inew_expr1_label.grid_remove()

inew_expr1_value = tk.Entry(root, font=fontStyle1)
inew_expr1_value.grid(row=3, column = 1)
inew_expr1_value.grid_remove()

inew_expr2_label = tk.Label(root, text = "Lista Y = ")
inew_expr2_label.grid(row=4, column = 0)
inew_expr2_label.grid_remove()

inew_expr2_value = tk.Entry(root, font=fontStyle1)
inew_expr2_value.grid(row=4, column = 1)
inew_expr2_value.grid_remove()

inew_expr3_label = tk.Label(root, text = "Encontrar X = ")
inew_expr3_label.grid(row=5, column = 0)
inew_expr3_label.grid_remove()

inew_expr3_value = tk.Entry(root, font=fontStyle1)
inew_expr3_value.grid(row=5, column = 1)
inew_expr3_value.grid_remove()

inew_bt = tk.Button(root, text = "=", command = conta_iNewton)
inew_bt.grid(row=6, column = 1)
inew_bt.config(height = 2, width = 5)
inew_bt.grid_remove()

inew_result = tk.Entry(root,font = fontStyle1)
inew_result.grid(row=7, column = 1)
inew_result.grid_remove()

root.mainloop()