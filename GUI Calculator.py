# ||Calculator MK6 by Alvin Fung||

import tkinter as tk
from tkinter import *
#can also use "import tkinter as tk" or "from tkinter import *"

# global expression - this will store the result of calculations.
operation = ""

def add_to_operation(symbol):
    global operation #allows to be manipulated inside a function
    
    operation += str(symbol)
    window_result.delete(1.0 , "end") #first index position, last index position
    #The 1 is the first line and the 0 is before the first character, "end" is end of text
    window_result.insert(1.0, operation) #index position, string

def evaluate_operation():
    global operation
    try:
        opeartion = str(eval(operation))
        operation = ""
        window_result.delete(1.0, "end") 
        window_result.insert(1.0, operation) 
    
    except:
        clear_operation()
        window_result.insert(1.0, "Error Ocurred")
        pass

def clear_operation():
    global operation
    operation = ""
    window_result.delete(1.0, "end")

window = tk.Tk() #This is the top level widget of Tk - represents mostly the main window of an application.
window.title("Calculator MK6")
window.geometry("300x275")
window_result = tk.Text(window, height=2, width=16, font=("Roboto Mono", 24)) #Establish the result's dimensions.
window_result.grid(columnspan = 5)


#Buttons
btn_1 = Button(window, text ="1", command = lambda: add_to_operation(1), width = 5, font = ("Roboto Mono", 24))
btn_1.grid(row = 2, column = 1)

btn_2 = Button(window, text ="2", command = lambda: add_to_operation(2), width = 5, font = ("Roboto Mono", 24))
btn_2.grid(row = 2, column = 2)

btn_3 = Button(window, text ="3", command = lambda: add_to_operation(3), width = 5, font = ("Roboto Mono", 24))
btn_3.grid(row = 2, column = 3)

btn_4 = Button(window, text ="4", command = lambda: add_to_operation(4), width = 5, font = ("Roboto Mono", 24))
btn_4.grid(row = 3, column = 1)

btn_5 = Button(window, text ="5", command = lambda: add_to_operation(5), width = 5, font = ("Roboto Mono", 24))
btn_5.grid(row = 3, column = 2)

btn_6 = Button(window, text ="6", command = lambda: add_to_operation(6), width = 5, font = ("Roboto Mono", 24))
btn_6.grid(row = 3, column = 3)

btn_7 = Button(window, text ="7", command = lambda: add_to_operation(7), width = 5, font = ("Roboto Mono", 24))
btn_7.grid(row = 4, column = 1)

btn_8 = Button(window, text ="8", command = lambda: add_to_operation(8), width = 5, font = ("Roboto Mono", 24))
btn_8.grid(row = 4, column = 2)

btn_9 = Button(window, text ="9", command = lambda: add_to_operation(9), width = 5, font = ("Roboto Mono", 24))
btn_9.grid(row = 4, column = 3)

btn_0 = Button(window, text ="0", command = lambda: add_to_operation(0), width = 5, font = ("Roboto Mono", 24))
btn_0.grid(row = 5, column = 2)

btn_plus = Button(window, text ="+", command = lambda: add_to_operation("+"), width = 5, font = ("Roboto Mono", 24))
btn_plus.grid(row = 2, column = 4)

window.mainloop()
