# ||Calculator MK6 by Alvin Fung||

import tkinter as tk

# global operation ???
operation = ""

def addToOperation(symbol):
    global operation #allows to be manipulated inside a function
    
    operation = operation + str(symbol)
    

def evaluateOperation():
    pass #This will have to be changed in the future, and likewise for clearOperation()

def clearOperation():
    pass


window = tk.Tk()
window.title("Calculator MK6")
window.geometry("300x275")
window_result = tk.Text(window, height=2, width=16, font=("Roboto Mono", 24)) #Establish the result's dimensions
window_result.grid(columnspan =5)
window.mainloop()


#Function to deal with the input operations
def input(num):

    global operation
    operation = operation + str(num)
