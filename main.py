import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("calculator")
        self.geometry("380x420")
        self.result = tk.Entry(self, font=("arial", 20))
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=20, ipady=15)
        self.result.config(justify=tk.LEFT)

        bt_frame1 = tk.Frame(self)
        bt_frame1.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.button("1", bt_frame1, 0, 0, lambda: self.number(1), bg="lightgrey")
        self.button("2", bt_frame1, 0, 1, lambda: self.number(2), bg="lightgrey")
        self.button("3", bt_frame1, 0, 2, lambda: self.number(3), bg="lightgrey")
        self.button("4", bt_frame1, 1, 0, lambda: self.number(4), bg="lightgrey")
        self.button("5", bt_frame1, 1, 1, lambda: self.number(5), bg="lightgrey")
        self.button("6", bt_frame1, 1, 2, lambda: self.number(6), bg="lightgrey")
        self.button("7", bt_frame1, 2, 0, lambda: self.number(7), bg="lightgrey")
        self.button("8", bt_frame1, 2, 1, lambda: self.number(8), bg="lightgrey")
        self.button("9", bt_frame1, 2, 2, lambda: self.number(9), bg="lightgrey")
        self.button("0", bt_frame1, 3, 1, lambda: self.number(0), bg="lightgrey")
        self.button("+", bt_frame1, 1, 3, lambda: self.operation("+"), bg="lightblue")
        self.button("-", bt_frame1, 2, 3, lambda: self.operation("-"), bg="lightblue")
        self.button("*", bt_frame1, 3, 3, lambda: self.operation("*"), bg="lightblue")
        self.button("/", bt_frame1, 3, 2, lambda: self.operation("/"), bg="lightblue")
        self.button("=", bt_frame1, 3, 0, self.calculate, bg="lightgreen")
        self.button("C", bt_frame1, 0, 3, self.clear, bg="orange")

    def button(self, text, frame, row, column, command, bg="white"):
        button = tk.Button(frame, text=text, command=command, width=5, height=3)
        button.config(bg=bg)
        button.grid(row=row, column=column, padx=10, pady=10)

    def number(self, number):
        current = self.result.get()
        current += str(number)
        self.result.delete(0, tk.END)
        self.result.insert(0, current)

    def operation(self, operator):
        current = self.result.get()
        current += operator
        self.result.delete(0, tk.END)
        self.result.insert(0, current)

    def calculate(self):
        current = self.result.get()
        self.result.delete(0, tk.END)
        self.result.insert(0, eval(current))

    def clear(self):
        self.result.delete(0, tk.END)

if __name__ == "__main__":
    Calculator = Calculator()
    Calculator.mainloop()
