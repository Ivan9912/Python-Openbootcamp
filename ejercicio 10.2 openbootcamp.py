"""
    En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
"""

import tkinter as tk

def Exit():
    window.quit()

# def select():
#     cadena = f'{listItems.get()}'
#     print(cadena)
#     labe2.config(text=cadena)

liste = ['Option one', 'Option two', 'Option three', 'Option four', 'Option five', 'Option six', 'Option seven', 'Option eigth', 'Option nine', 'Option ten']

window = tk.Tk()
window.columnconfigure(0, weight=3)

listItems = tk.StringVar(value=liste)


listbox = tk.Listbox(window, listvariable=listItems, border=1)
listbox.grid(column=0, row=0, padx=5, pady=5)
# listbox.bind('Double-1', select)

label = tk.Label(window, text='Eligió:')
label.grid(column=0, row=8, padx=5, pady=5, sticky=tk.W)
# labe2 = tk.Label(window, text='hola')
# labe2.grid(column=0, row=8, padx=5, pady=5)
botonExit = tk.Button(window, text='_Exit_', command=Exit)
botonExit.grid(column=1, row=0, padx=5, pady=5, sticky=tk.E)
window.mainloop()