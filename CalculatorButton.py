import tkinter as tk
from tkinter import *

class CalculatorButton(tk.Button):
    
    def __init__(self, parent, text, function):
        super().__init__(parent, text=text, command=function) #Inheritance
        self.attributes = {
            "bg":'grey25', "font": ('Roboto Mono', 24),
            "width":'5',"padx":'5', "pady": '5'}
        self.config(self.attributes)
