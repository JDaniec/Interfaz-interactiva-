from tkinter import *
#se importa a la librería tekinter con todas las funciones from tkinter import

#----------------
#Funciones de la app
#----------------

#-----------------
#Ventana principal
#-----------------

#se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto TK 

ventana_principal = Tk()

#titulo de la ventina
ventana_principal.title("Sistemas UIS socorro")

#tamaño de la ventana
ventana_principal.geometry("500x500")

#deshabilitar botón de maximizar
ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="thistle4")

#----------------------
#frame entrada d#e datos
#----------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="yellow",width = 500, height = 250)
frame_entrada.place(x=0, y=0)

#------------------------
#frame operaciones
#------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "blue",width=500,height=125)
frame_operaciones.place(x=0,y=250)

#-----------------
#frame resultados
#----------------

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg = "red",width = 500, height = 125)
frame_resultados.place(x=0,y=375)


ventana_principal.mainloop()

