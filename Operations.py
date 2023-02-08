import tkinter as tk
from tkinter import *


class Operations(tk.Text):

    def __init__(self, parent, height, width, font):
        super().__init__(parent, height=height, width=width, font=font)
        # self expression - this will store the result of calculations.
        self.operation = ""

    def add_to_operation(self, symbol):

        self.operation += str(symbol)
        self.delete(1.0, "end")  # first index position, last index position
        # The 1 is the first line and the 0 is before the first character, "end" is end of text
        self.insert(1.0, self.operation)  # index position, string

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

    def ans_operation(self):
        try:
            ans = self.result + self.add_to_operation()
            self.delete(1.0, "end")
            self.insert(1.0, ans)

        except:
            self.clear_operation()
            self.insert(1.0, "Incorrect Syntax")
            pass
