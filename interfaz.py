from tkinter import *
from tkinter import messagebox
#se importa a la librería tekinter con todas las funciones from tkinter import

#----------------
#Funciones de la app
#----------------
def calcular():
    messagebox.showinfo("minicalculadora1.0", "Hizo click en el boton calcular")
    s = int(a.get()) + int(b.get())
    t_resultados.insert(INSERT, f"{a.get()} + {b.get()} = {s} \n")
    r = int(a.get()) - int(b.get())
    t_resultados.insert(INSERT, f"{a.get()} - {b.get()} = {r} \n")
    d = int(a.get()) / int(b.get())
    t_resultados.insert(INSERT, f"{a.get()} / {b.get()} = {d} \n")
    de = int(a.get()) // int(b.get())
    t_resultados.insert(INSERT, f"{a.get()} // {b.get()} = {de} \n")
    m = int(a.get()) * int(b.get())
    t_resultados.insert(INSERT, f"{a.get()} * {b.get()} = {m} \n")
    mod = int(a.get()) % int(b.get())
    t_resultados.insert(INSERT, f"{a.get()} % {b.get()} = {mod} \n")
    p = int(a.get()) ** int(b.get())
    t_resultados.insert(INSERT, f"{a.get()} ** {b.get()} = {p} \n")

def borrar():
    messagebox.showinfo("minicalculadora1.0", "Los datos serán borrados")
    a.set("")
    b.set("")
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("minicalculadora1.0", "La app se cerrará")
    ventana_principal.destroy()
    
#-----------------
#Ventana principal
#-----------------

#se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto TK 

ventana_principal = Tk()

#titulo de la ventina
ventana_principal.title("Minicalculadora")

#tamaño de la ventana
ventana_principal.geometry("500x500")

#deshabilitar botón de maximizar
ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="thistle4")

#----------------------
#variables de control
#----------------------
a = StringVar()
b = StringVar()

#----------------------
#frame entrada d#e datos
#----------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white",width = 480, height = 180)
frame_entrada.place(x=10, y=10)

#Logo de la app

logo = PhotoImage(file="img/logo_uis.png")
lb_logo = Label(frame_entrada, image=logo, bg ="White")
lb_logo.place(x=11, y = 40)


#etiqueta para el titulo
lb_titulo=Label(frame_entrada, text= "Mini calculadora 1.0")
lb_titulo.config(bg="White", fg="Green", font=("Herlvetica" , 19))
lb_titulo.place(x=240 , y=10)


#etiqueta para el primer numero
lb_a = Label(frame_entrada, text= "a: ")
lb_a.config(bg="White" , fg="Green", font=("Herlvetica" , 20))
lb_a.place(x=250, y = 60)

#Caja de texto
entry_a = Entry(frame_entrada, textvariable= a)
entry_a.config(bg= "white", fg="Green", font=("Courtier" , 20))
entry_a.focus_set()
entry_a.place(x=290 , y=60, width=100, height=30)
#-----------------------------
lb_b = Label(frame_entrada, text= "b: ")
lb_b.config(bg="White" , fg="Green", font=("Herlvetica" , 20))
lb_b.place(x=250, y = 100)

#--------------------------------
entry_b = Entry(frame_entrada, textvariable= b)
entry_b.config(bg= "white", fg="Green", font=("Courtier" , 20))
entry_b.place(x=290 , y=100, width=100, height=30)

#------------------------
#frame operaciones
#------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "white",width=480,height=100)
frame_operaciones.place(x=10 ,y=200)

#calcular
bt_calcular = Button(frame_operaciones, text = "Calcular", command = calcular)
bt_calcular.place(x = 45, y = 35, width = 100, height=30)

#borrar
bt_borrar = Button(frame_operaciones, text = "Borrar", command = borrar)
command = borrar
bt_borrar.place(x = 190, y = 35, width = 100, height=30)

#salir
bt_salir = Button(frame_operaciones, text = "Salir", command = salir)
bt_salir.place(x = 335, y = 35, width = 100, height=30)


#-----------------
#frame resultados
#----------------

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg = "white",width = 480, height = 180)
frame_resultados.place(x=10,y=310)

#area para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="Black", fg="Green", font=("Courtier" , 20))
t_resultados.place(x =10 , y = 10, width=460, height=160)




ventana_principal.mainloop()

