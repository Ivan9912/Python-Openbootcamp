"""
    En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
    Al principio no tiene que haber una opción seleccionada.
"""
import tkinter as tk
from tkinter import ttk

def exit():
    window.quit()
def radioSelect():
    cadena = f'{list_select.get()}'
    visualizar2.config(text=cadena)
def reset():
    list_select.set(None)
    visualizar2.config(text='')

window = tk.Tk()
window.columnconfigure(0, weight=3)
list_select = tk.StringVar()
list_select.set(None)

radio1 = ttk.Radiobutton(window, text='Option one', variable=list_select, command=radioSelect, value='Inglés')
radio1.grid(column=0,row=1,padx=5,pady=5, sticky=tk.W)
radio2 = ttk.Radiobutton(window, text='Option two', variable=list_select, command=radioSelect, value='Español')
radio2.grid(column=0,row=2,padx=5,pady=5, sticky=tk.W)
radio3 = ttk.Radiobutton(window, text='Option three', variable=list_select, command=radioSelect, value='Alemán')
radio3.grid(column=0,row=3,padx=5,pady=5, sticky=tk.W)

visualizar1 = ttk.Label(window)
visualizar1.grid(column=0,row=5,padx=5,pady=5, sticky=tk.E)
visualizar1.config(text='Eligió:')
visualizar2 = ttk.Label(window)
visualizar2.grid(column=1,row=5,padx=5,pady=5, sticky=tk.W)

botonReset = ttk.Button(window, text='reset', command=reset)
botonReset.grid(column=0,row=4,padx=5,pady=5)

botonSalir = ttk.Button(window, text='Exit', command=exit)
botonSalir.grid(column=1, row=4,padx=5,pady=5)

window.mainloop()