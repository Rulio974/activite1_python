import operator
from tkinter import *
from tkinter import ttk
from turtle import width
from Moteur import *



class Gestion(Frame):
    def __init__(self, root, w, atelier, cb_add, cb_mod, cb_del):
        Frame.__init__(self, root)

        self.atelier = atelier
        self.w = w

        tableau = ttk.Treeview(self, selectmode="browse", height=20)
        tableau.pack(side=TOP, fill=BOTH, expand=True)
        self.tableau = tableau

        tableau['columns'] = ['LBL'] + ["M"+str(j+1) for j in range(0, 
        self.atelier.machine)]+["Début", "Fin"]       


        labels = ['Label'] + ["Temps sur M"+str(j+1) for j in range(0,
        self.atelier.machine)]+["Début", "Fin"]
        print("il y a %d machines" % self.atelier.machine)
        nb_machine = self.atelier.machine

        for idx, colonne in enumerate(tableau['columns']):
            tableau.column(colonne, width=self.w//int(nb_machine+3))
            tableau.heading(colonne,text=labels[idx],anchor=CENTER)


        tableau.column("#0", width=0, stretch=NO)
        tableau.heading("#0", text="", anchor=CENTER)
        
      
        self.remplir_tableau()
        
    
    def remplir_tableau(self):
        for i in self.tableau.get_children():
            self.tableau.delete(i)

        for i in range(0, self.atelier.machine):
            self.tableau.insert(parent='', index='end', iid=i, 
            values=[self.atelier.dict['taches'][i]['label'], 
            self.atelier.dict['taches'][i]['p'][0],
            self.atelier.dict['taches'][i]['p'][1]])
    



