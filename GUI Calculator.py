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

#Frames - This is required in order to switch between two variations of the calculator for different operations

# class Stack(tk.frame): #This handles the stack order of the frames
    
#     def __init__(self, *args, **kwargs):
#         window.__init__(self, *args, **kwargs)

#         #The container is where the frames will be stacked
#         #on top of each other, then the one want present
#         #will be raised above the others
#         container = tk.window(self)
#         container.pack()

#         self.window = {}
#         for F in (Standard, Scientific):
#             page_name = F.__name__
#             window = F(parent = container, controller = self)
#             self.frames[page_name] = window
            
#             window.geometry("460x435")
#             window.minsize(460,435)
#             window.maxsize(460,435)
            
#         self.show_window("Standard")
    
#     def show_window(self, page_name):
#         window = self.windows[page_name]
#         window.tkraise()

# THIS NEEDS MORE WORKING ON.

# class Standard(tk.frame):
#     pass

# class Scientific(tk.Frame):
#     pass


# Window Management
window = tk.Tk() #This is the top level widget of Tk - represents mostly the main window of an application.
window.title("Calculator MK 6")
window.configure(background = "grey15")
window.geometry("460x435")
window.minsize(460,435)
window.maxsize(460,435)
window_result = tk.Text(window, height=2, width=16, font=("Roboto Mono", 24)) #Establish the result's dimensions.
window_result.grid(columnspan = 5)


#Buttons
# switch = Button(window, text = "Mode", command = lambda: pass)

class button(Button):
    
    def __init__(self, text, row, col, command, bg, **kwargs):
        Button.__init__(self,text, row, col, command,bg, **kwargs)
        self.text = text
        self.row = row
        self.column = col
        self.command = command
        self['bg'] =  self.color
        self['text'] = self.text
        self['command'] = self.command
        row.grid(row = self.row, column = self.column)
        


btn_1 = button("1", 2, 1, add_to_operation(1),'grey25')

# btn_1 = Button(window, text ="1", command = lambda: add_to_operation(1), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
# btn_1.grid(row = 2, column = 1, padx = 5, pady = 5)

btn_2 = Button(window, text ="2", command = lambda: add_to_operation(2), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
btn_2.grid(row = 2, column = 2, padx = 5, pady = 5)

btn_3 = Button(window, text ="3", command = lambda: add_to_operation(3), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
btn_3.grid(row = 2, column = 3, padx = 5, pady = 5)

btn_4 = Button(window, text ="4", command = lambda: add_to_operation(4), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
btn_4.grid(row = 3, column = 1, padx = 5, pady = 5)

btn_5 = Button(window, text ="5", command = lambda: add_to_operation(5), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
btn_5.grid(row = 3, column = 2, padx = 5, pady = 5)

btn_6 = Button(window, text ="6", command = lambda: add_to_operation(6), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
btn_6.grid(row = 3, column = 3, padx = 5, pady = 5)

btn_7 = Button(window, text ="7", command = lambda: add_to_operation(7), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
btn_7.grid(row = 4, column = 1, padx = 5, pady = 5)

btn_8 = Button(window, text ="8", command = lambda: add_to_operation(8), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
btn_8.grid(row = 4, column = 2, padx = 5, pady = 5)

btn_9 = Button(window, text ="9", command = lambda: add_to_operation(9), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
btn_9.grid(row = 4, column = 3, padx = 5, pady = 5)

btn_0 = Button(window, text ="0", command = lambda: add_to_operation(0), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
btn_0.grid(row = 5, column = 2, padx = 5, pady = 5)

add = Button(window, text ="+", command = lambda: add_to_operation("+"), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
add.grid(row = 2, column = 4, padx = 5, pady = 5)

minus = Button(window, text = "-", command = lambda: add_to_operation("-"), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
minus.grid(row = 3, column = 4, padx = 5, pady = 5)

mul = Button(window, text = "*", command = lambda: add_to_operation("*"), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
mul.grid(row = 4, column = 4, padx = 5, pady = 5)

div = Button(window, text = "/", command = lambda: add_to_operation("/"), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
div.grid(row = 5, column = 4, padx = 5, pady = 5)

l_bracket = Button(window, text = "(", command = lambda: add_to_operation("("), width = 5,font = ("Roboto Mono", 24), bg = "grey25")
l_bracket.grid(row = 5, column = 1, padx = 5, pady = 5)

r_bracket = Button(window, text = ")", command = lambda: add_to_operation(")"), width = 5, font = ("Roboto Mono", 24), bg = "grey25")
r_bracket.grid(row = 5, column = 3, padx = 5, pady = 5)

decimal = Button(window, text = ".", command = lambda: add_to_operation("."), width = 5, font = ("Roboto Mons", 24), bg = "grey25")
decimal.grid(row = 6, column = 1, columnspan = 2, padx = 5, pady = 5)

clear = Button(window, text = "C", command = clear_operation, width = 5,font = ("Roboto Mono", 24), bg = "grey25")
clear.grid(row = 6, column = 2, columnspan = 2, padx = 5, pady = 5)

equals = Button(window, text = "=", command = evaluate_operation, width = 5, font = ("Roboto Mono", 24), bg = "grey25")
equals.grid(row = 6, column = 3, columnspan = 2, padx = 5, pady = 5)

# if __name__ ==  "__main__":
#     window = Stack()
#     window.mainloop()

window.mainloop()
