from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
from Gestion import *
import Moteur
 
atelier = Moteur.Atelier()
atelier.load()

class window:
    def __init__(self):
        self.window = Tk()
        self.window.option_add('*foreground', 'black')
        self.window.tk.call("source", "azure.tcl")
        self.window.tk.call("set_theme", "dark")
        self.window.title("Gestion Atelier")
    
        plus=PhotoImage(file="assets/plus.png")
        reload=PhotoImage(file="assets/reload.png")
        calcul=PhotoImage(file="assets/calcul.png")
        sauvegarder=PhotoImage(file="assets/sauvegarder.png")

        #Button(self.window, text="N", height=2, width=10, bg='#567', fg='White', borderwidth = 2).grid(sticky="W", row = 0, column = 0)

        self.tabControl = ttk.Notebook(self.window, width=1100, height=700)
        onglet1 = Gestion(self.tabControl, 1090, atelier, None, None, None)
        onglet2 = Frame(self.tabControl)

        Label(self.window, text="").grid(row=1, column=0, columnspan=4)

        self.b1 = Button(self.window, image=plus, height= 50, width=50 ,bg='#737373', fg='White', borderwidth = 0).grid(sticky="W", row = 2, column = 1)
        self.b2 = Button(self.window, image=reload, height=50, width=50, bg='#737373', fg='White', borderwidth = 0).grid(sticky="W", row = 2, column = 2)
        self.b3 = Button(self.window, image=calcul, height=50, width=50, bg='#737373', fg='White', borderwidth = 0).grid(sticky="W", row = 2, column = 3)
        self.b4 = Button(self.window, image = sauvegarder, height=50, width=50, bg='#737373', fg='White', borderwidth = 0).grid(sticky="W", row = 2, column = 4)

        Label(self.window, text="").grid(row=3, column=0, columnspan=4)



        self.tabControl.add(onglet1, text='Gestion des tâches')
        self.tabControl.add(onglet2, text='Ordonnancement')

        self.tabControl.grid(row = 4, column = 0, columnspan = 100)

        self.window.mainloop()


    
window()