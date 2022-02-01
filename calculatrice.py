
from tkinter import *

class myWindow:
    def __init__(self):
        self.count = 0
        self.window = Tk()
        self.window.title("Calculatrice")
        self.window.geometry("500x200")
        self.label = Label(self.window, text=str(self.count), 
        font=("Courrier", 30, 'bold')).grid(row=0, column=0, columnspan=2)
        
        #modifier couleur de bordure d'un bouton

        Button(self.window, text="1", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=1, column=0)
        Button(self.window, text="2", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=1, column=1)
        Button(self.window, text="3", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=1, column=2)
        Button(self.window, text="4", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=2, column=0)
        Button(self.window, text="5", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=2, column=1)
        Button(self.window, text="6", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=2, column=2)
        Button(self.window, text="7", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=3, column=0)
        Button(self.window, text="8", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=3, column=1)
        Button(self.window, text="9", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=3, column=2)
        Button(self.window, text="0", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=4, column=0)
        Button(self.window, text="/", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=1, column=4)
        Button(self.window, text="*", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=2, column=4)
        Button(self.window, text="-", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=3, column=4)
        Button(self.window, text="+", command=lambda:self.addDigit, height=2, width=4, bg='#567', fg='White', borderwidth = 0).grid(row=4, column=4)

        Button(self.window, text="=", command=lambda:self.addDigit, height=2, width=9 , bg='#567', fg='White', borderwidth = 0).grid(row = 4, column = 1,  columnspan= 2)

      

        self.window.mainloop()

myWindow()



