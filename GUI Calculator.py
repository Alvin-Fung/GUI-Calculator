# ||Calculator MK6 by Alvin Fung||

import tkinter as tk
from tkinter import *

class Operations(tk.Text):
 
    def __init__(self, parent, height, width, font):
        super().__init__(parent, height = height, width = width, font = font)
        self.operation = "" # self expression - this will store the result of calculations.

    def add_to_operation(self,symbol):
        
        self.operation += str(symbol)
        self.delete(1.0 , "end") #first index position, last index position
        #The 1 is the first line and the 0 is before the first character, "end" is end of text
        self.insert(1.0, self.operation) #index position, string

    def evaluate_operation(self):
        
        try:
            result = str(eval(self.operation))
            # print(result)
            self.operation = ""
            self.delete(1.0, "end") 
            self.insert(1.0, result) 
        
        except:
            self.clear_operation()
            self.insert(1.0, "Incorrect Syntax")
            pass

    def clear_operation(self):
        self.operation = ""
        self.delete(1.0, "end")


class Window(tk.Tk):# Window Management
    def __init__(self):
        super().__init__()
        self.title("Calculator MK6")
        self.attributes = {
            "bg":"grey15", "width": '460', "height": '435',
            }
        self.maxsize = (460, 435)
        self.minxsize = (460, 435)
        self.configure(self.attributes)


class StandardPage(tk.Frame):

     def __init__(self, parent):
        super().__init__(parent)
        self.window_result = Operations(self, height=2, width=16, font=("Roboto Mono", 24)) #Establish the result's dimensions.
        self.window_result.grid(columnspan = 5)
        
       
        btn_1 = CalculatorButton(self, "1", lambda: self.window_result.add_to_operation(1))
        btn_1.grid(row = 2, column  = 1)

        btn_2 = CalculatorButton(self, "2", lambda: self.window_result.add_to_operation(2))
        btn_2.grid(row = 2, column = 2)

        btn_3 = CalculatorButton(self, "3", lambda: self.window_result.add_to_operation(3))
        btn_3.grid(row = 2, column = 3)

        btn_4 = CalculatorButton(self, "4", lambda: self.window_result.add_to_operation(4))
        btn_4.grid(row = 3, column = 1)

        btn_5 = CalculatorButton(self, "5", lambda: self.window_result.add_to_operation(5))
        btn_5.grid(row = 3, column = 2)

        btn_6 = CalculatorButton(self, "6", lambda: self.window_result.add_to_operation(6))
        btn_6.grid(row = 3, column = 3)

        btn_7 = CalculatorButton(self, "7", lambda: self.window_result.add_to_operation(7))
        btn_7.grid(row = 4, column = 1)

        btn_8 = CalculatorButton(self, "8", lambda: self.window_result.add_to_operation(8))
        btn_8.grid(row = 4, column = 2)

        btn_9 = CalculatorButton(self, "9", lambda: self.window_result.add_to_operation(9))
        btn_9.grid(row = 4, column = 3)

        btn_0 = CalculatorButton(self, "0", lambda: self.window_result.add_to_operation(0))
        btn_0.grid(row = 5, column = 2)

        add = CalculatorButton(self, "+", lambda: self.window_result.add_to_operation("+"))
        add.grid(row = 2, column = 4)

        minus = CalculatorButton(self, "-", lambda: self.window_result.add_to_operation("-"))
        minus.grid(row = 3, column = 4)

        mul = CalculatorButton(self, "*", lambda: self.window_result.add_to_operation("*"))
        mul.grid(row = 4, column = 4)

        div = CalculatorButton(self, "/", lambda: self.window_result.add_to_operation("/"))
        div.grid(row = 5, column = 4)

        l_bracket = CalculatorButton(self, "(", lambda: self.window_result.add_to_operation("("))
        l_bracket.grid(row = 5, column = 1)

        r_bracket = CalculatorButton(self, ")", lambda: self.window_result.add_to_operation(")"))
        r_bracket.grid(row = 5, column = 3)

        decimal = CalculatorButton(self,".", lambda: self.window_result.add_to_operation("."))
        decimal.grid(row = 6, column = 1, columnspan = 2)

        clear = CalculatorButton(self, "C", self.window_result.clear_operation)
        clear.grid(row = 6, column = 2, columnspan = 2)

        equals = CalculatorButton(self, "=", self.window_result.evaluate_operation)
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

window = Window()
page = StandardPage(window)
window.mainloop()
