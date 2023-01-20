# ||Calculator MK6 by Alvin Fung||

import tkinter as tk
from tkinter import *

# global expression - this will store the result of calculations.
operation = ""

class Operations(tk.Text):
 
    def add_to_operation(symbol):
        global operation #allows to be manipulated inside a function
        
        operation += str(symbol)
        window_result.delete(1.0 , "end") #first index position, last index position
        #The 1 is the first line and the 0 is before the first character, "end" is end of text
        window_result.insert(1.0, operation) #index position, string

    def evaluate_operation():
        global operation
        # print(operation)
        try:
            result = str(eval(operation))
            # print(result)
            operation = ""
            window_result.delete(1.0, "end") 
            window_result.insert(1.0, result) 
        
        except:
            clear_operation()
            window_result.insert(1.0, "Incorrect Syntax")
            pass

    def clear_operation():
        global operation
        operation = ""
        window_result.delete(1.0, "end")

# Window Management
#Frames - This is required in order to switch between two variations of the calculator for different operations

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator MK6")
        self.configure(background = "grey15", width = 460, height = 435)

class StandardPage(tk.Frame, Operations):
     def __init__(self, parent):
        #This is the top level widget of Tk - represents mostly the main window of an application.
        super().__init__(parent)
        window_result = tk.Text(self, height=2, width=16, font=("Roboto Mono", 24)) #Establish the result's dimensions.
        window_result.grid(columnspan = 5)
        
        btn_1 = CalculatorButton(self, "1", lambda: add_to_operation(1))
        btn_1.grid(row = 2, column  = 1,)

        btn_2 = CalculatorButton(self, "2", lambda: add_to_operation(2))
        btn_2.grid(row = 2, column = 2)

        btn_3 = CalculatorButton(self, "3", lambda: add_to_operation(3))
        btn_3.grid(row = 2, column = 3)

        btn_4 = CalculatorButton(self, "4", lambda: add_to_operation(4))
        btn_4.grid(row = 3, column = 1)

        btn_5 = CalculatorButton(self, "5", lambda: add_to_operation(5))
        btn_5.grid(row = 3, column = 2)

        btn_6 = CalculatorButton(self, "6", lambda: add_to_operation(6))
        btn_6.grid(row = 3, column = 3)

        btn_7 = CalculatorButton(self, "7", lambda: add_to_operation(7))
        btn_7.grid(row = 4, column = 1)

        btn_8 = CalculatorButton(self, "8", lambda: add_to_operation(8))
        btn_8.grid(row = 4, column = 2)

        btn_9 = CalculatorButton(self, "9", lambda: add_to_operation(9))
        btn_9.grid(row = 4, column = 3)

        btn_0 = CalculatorButton(self, "0", lambda: add_to_operation(0))
        btn_0.grid(row = 5, column = 2)

        add = CalculatorButton(self, "+", lambda: add_to_operation("+"))
        add.grid(row = 2, column = 4)

        minus = CalculatorButton(self, "-", lambda: add_to_operation("-"))
        minus.grid(row = 3, column = 4)

        mul = CalculatorButton(self, "*", lambda: add_to_operation("*"))
        mul.grid(row = 4, column = 4)

        div = CalculatorButton(self, "/", lambda: add_to_operation("/"))
        div.grid(row = 5, column = 4)

        l_bracket = CalculatorButton(self, "(", lambda: add_to_operation("("))
        l_bracket.grid(row = 5, column = 1)

        r_bracket = CalculatorButton(self, ")", lambda: add_to_operation(")"))
        r_bracket.grid(row = 5, column = 3)

        decimal = CalculatorButton(self,".", lambda: add_to_operation("."))
        decimal.grid(row = 6, column = 1, columnspan = 2)

        clear = CalculatorButton(self, "C", clear_operation)
        clear.grid(row = 6, column = 2, columnspan = 2)

        equals = CalculatorButton(self, "=", evaluate_operation)
        equals.grid(row = 6, column = 3, columnspan = 2)

        self.pack()

#Buttons
class CalculatorButton(tk.Button):
    
    def __init__(self, parent, text, function):
        super().__init__(parent, text=text, command=function) #Inheritance
        self.attributes = {
            "bg":'grey25', "font": ('Roboto Mono', 24),
            "width":'5',"padx":'5', "pady": '5'}
        self.config(self.attributes)

window_result = tk.Text(height=2, width=16, font=("Roboto Mono", 24)) #Establish the result's dimensions.
window = Window()
page = StandardPage(window)
window.mainloop()
