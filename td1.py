from tkinter import *

class myWindow:
    def __init__(self):
        self.count = 0
        self.window = Tk()
        self.window.title("Test")
        self.window.geometry("500x200")
        self.label = Label(self.window, text=str(self.count), 
        font=("Courrier", 30, 'bold'))
        self.label.pack(padx=5, pady=5, fill=BOTH, expand=1)
        
        b1 = Button(self.window, text="-", command=self.decrement)
        b2 = Button(self.window, text="+", command=self.increment)
        
        b1.pack(side=LEFT, fill=X, expand=1, padx=5, pady=5)
        b2.pack(side=RIGHT, fill=X, expand=1, padx=5, pady=5)

        self.window.mainloop()

    def increment(self):
        self.count+=1
        self.label.config(text=str(self.count))

    def decrement(self):
        self.count-=1
        self.label.config(text=str(self.count))



myWindow()



