from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera de noruega :)")

ventana_principal.geometry("700x400")

ventana_principal.resizable(0,0)

#------------------------------------
ventana_principal.config(bg = "Red")


#-------------------------------------
frame_entrada= Frame(ventana_principal)
frame_entrada.config(bg = "white", width=100, height= 400)
frame_entrada.place(x = 200, y = 0)

#-------------------------------------
frame_config = Frame(ventana_principal)
frame_config.config(bg = "White", width=700, height=100)
frame_config.place(x = 0, y = 150)

#----------------------------------------
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg = "Blue", width=50, height=400)
frame_resultados.place(x = 225, y = 0)

#----------------------------------------
frame_final = Frame(ventana_principal)
frame_final.config(bg = "Blue", width=700, height=50)
frame_final.place(x = 0, y = 175)
ventana_principal.mainloop()


