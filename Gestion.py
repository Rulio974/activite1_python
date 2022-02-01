import operator
from tkinter import *
from tkinter import ttk
from turtle import width
from Moteur import *



class Gestion(Frame):
    def __init__(self, root, w, atelier, cb_add, cb_mod, cb_del):
        Frame.__init__(self, root)

        self.atelier = atelier
        tableau = ttk.Treeview(self, selectmode="browse", height=20)
        tableau.pack(side=TOP, fill=BOTH, expand=True)
        self.tableau = tableau

        tableau['columns'] = ['LBL'] + ["M"+str(j+1) for j in range(0, 
        self.atelier.machine)]+["Début", "Fin"]       


        labels = ['Label'] + ["Temps sur M"+str(j+1) for j in range(0,
        self.atelier.machine)]+["Début", "Fin"]


        for idx, colonne in enumerate(tableau['columns']):
            tableau.column(colonne, width= operator.floordiv( 3, 3))
            tableau.heading(colonne,text=labels[idx],anchor=CENTER)


        tableau.column("#0", width=0, stretch=NO)
        tableau.heading("#0", text="", anchor=CENTER)

