#Lo más básico ya esta listo, falta darle una interfaz interactiva con el usuario y un despliegue más estético de los datos

from tkinter import *
import tkinter as tk
from tkinter import ttk             #Módulos importados y variables de otro archivo
from tiempo import data, my_list

app = Tk()

frm = ttk.Frame(app, padding=10)
frm.grid()
c = 0                                       #variables arbitrarias
x = 1

def desplegar():
    global c
    global x
    for i in data():
        c += 1
        x += 1                                                              #Reproductor de elementos del archivo my_list
        texto = ttk.Label(frm, text=i).grid(column=2, row=c + 1)

c = 0
entry = ttk.Entry(frm, foreground='blue')
entry.grid(column=0, row=0)
label = ttk.Label(frm, text='hola')
label.grid(column=1, row=0)

def remove_text():
    label.config(text='')


def mostrar():
    print(entry.get())
    one = entry.get()
    global c
    i = 0
    l = my_list

    for j in l:
        print(j)
        if one in j:
            break
        else:
            i += 1
        print(i)
        
    print(my_list[i][2])
    label.config(text=my_list[i][2])
    label.grid(column=1, row=1)

ttk.Button(frm, text='Enter', command=mostrar).grid(column=0, row=1)
ttk.Button(frm, text="Delete", command=remove_text).grid(column=0, row=2)
ttk.Button(frm, text='Desplegar', command=desplegar).grid(column=0, row=3)
ttk.Button(frm, text="Quit", command=app.destroy).grid(column=0, row=4)             #Botón para cerrar la aplicación

app.mainloop()