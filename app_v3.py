import tkinter as tk
import tkinter.font as tkFont
import math
import bissecao as bissecao
import newton as newton

root = tk.Tk()
root.geometry("320x350")
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

def bt_Gauss():
    return

def bt_LU():
    return

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

# Fontes
fontStyle1 = tkFont.Font(family="Times", size=20)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=13)

##################################
biss_subtitle = tk.Button(root, text="Método da Bissecção",font = fontStyle2, command = bt_Bissecaao)
biss_subtitle.grid(row=0, column = 0)

new_subtitle = tk.Button(root, text="Método de Newton", font = fontStyle2, command = bt_Newton)
new_subtitle.grid(row=0, column = 1)

gauss_subtitle = tk.Button(root, text="Método de Gauss", font = fontStyle2, command = bt_Gauss)
gauss_subtitle.grid(row=1, column = 0)

lu_subtitle = tk.Button(root, text="Método de LU", font = fontStyle2, command = bt_LU)
lu_subtitle.grid(row=1, column = 1)
##################################

biss_emp = tk.Label(root, text="")
biss_emp.grid(row=2, column = 0)
biss_emp.grid_remove()

biss_a_label = tk.Label(root, text = "a = ")
biss_a_label.grid(row=3, column = 0)
biss_a_label.grid_remove()

biss_a_value = tk.Entry(root, font=fontStyle1, width=10)
biss_a_value.grid(row=3, column = 1)
biss_a_value.grid_remove()

biss_b_label = tk.Label(root, text = "b = ")
biss_b_label.grid(row=4, column = 0)
biss_b_label.grid_remove()

biss_b_value = tk.Entry(root, font=fontStyle1,width=10)
biss_b_value.grid(row=4, column = 1)
biss_b_value.grid_remove()

biss_epslon = tk.Label(root, text = "Epslon = ")
biss_epslon.grid(row=5, column = 0)
biss_epslon.grid_remove()

biss_epslon_value = tk.Entry(root, font=fontStyle1,width=10)
biss_epslon_value.grid(row=5, column = 1)
biss_epslon_value.grid_remove()

biss_bt = tk.Button(root, text = "=", command = conta_bissecaao)
biss_bt.grid(row=6, column = 1)
biss_bt.config(height = 2, width = 5)
biss_bt.grid_remove()

biss_result = tk.Entry(root,font = fontStyle1,width=10)
biss_result.grid(row=7, column = 1)
biss_result.grid_remove()

##############################################################################

new_emp = tk.Label(root, text="")
new_emp.grid(row=2, column = 0)
new_emp.grid_remove()

new_chute_label = tk.Label(root, text = "Chute = ")
new_chute_label.grid(row=3, column = 0)
new_chute_label.grid_remove()

new_chute_value = tk.Entry(root, font=fontStyle1,width=10)
new_chute_value.grid(row=3, column = 1)
new_chute_value.grid_remove()

new_epslon = tk.Label(root, text = "Epslon = ")
new_epslon.grid(row=4, column = 0)
new_epslon.grid_remove()

new_epslon_entry = tk.Entry(root, font=fontStyle1,width=10)
new_epslon_entry.grid(row=4, column = 1)
new_epslon_entry.grid_remove()

new_bt = tk.Button(root, text = "=", command = conta_newton)
new_bt.grid(row=5, column = 1)
new_bt.config(height = 2, width = 5)
new_bt.grid_remove()

new_result = tk.Entry(root,font = fontStyle1,width=10)
new_result.grid(row=6, column = 1)
new_result.grid_remove()

root.mainloop()