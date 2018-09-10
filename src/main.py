from tkinter import *
from tkinter import ttk
from sys import exit
if __name__ == "__main__":
    raiz = Tk()
    raiz.geometry('600x300')
    raiz.configure(bg = 'white')
    raiz.title('Aplicación')
    ttk.Button(raiz, text='Salir', command=sys.exit).pack(side=BOTTOM, pady=7)
    raiz.mainloop()