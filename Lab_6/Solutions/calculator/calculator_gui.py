import tkinter as tk
from tkinter.ttk import Button, Entry, Label
import parse_tree


class Calculator:
    equation_to_display = ""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")

        self.entry_display = Label(self.root,width=50, background="white")
        self.entry_display.grid(row=0, columnspan=5)

        self.result_display = Label(self.root, width=37, background="white")
        self.result_display.grid(row=1, columnspan=3)

        button_tree = Button(self.root, text="Tree")
        button_tree.grid(row = 0, column=5)

        button_one = Button(self.root, text="1", command=lambda: self.append_sign("1"))
        button_one.grid(row=2, column=0)

        button_two = Button(self.root, text="2", command=lambda: self.append_sign("2"))
        button_two.grid(row=2, column=1)

        button_three = Button(self.root, text="3", command=lambda: self.append_sign("3"))
        button_three.grid(row=2, column=2)

        button_four = Button(self.root, text="4", command=lambda: self.append_sign("4"))
        button_four.grid(row=3, column=0)

        button_five = Button(self.root, text="5", command=lambda: self.append_sign("5"))
        button_five.grid(row=3, column=1)

        button_six = Button(self.root, text="6", command=lambda: self.append_sign("6"))
        button_six.grid(row=3, column=2)

        button_seven = Button(self.root, text="7", command=lambda: self.append_sign("7"))
        button_seven.grid(row=4, column=0)

        button_eight = Button(self.root, text="8", command=lambda: self.append_sign("8"))
        button_eight.grid(row=4, column=1)

        button_nine = Button(self.root, text="9", command=lambda: self.append_sign("9"))
        button_nine.grid(row=4, column=2)

        button_plus = Button(self.root, text="+", command=lambda: self.append_sign("+"))
        button_plus.grid(row=5, column=0)

        button_minus = Button(self.root, text="-", command=lambda: self.append_sign("-"))
        button_minus.grid(row=5, column=1)

        button_zero = Button(self.root, text="0", command=lambda: self.append_sign("0"))
        button_zero.grid(row=5, column=2)

        button_mul = Button(self.root, text="*", command=lambda: self.append_sign("*"))
        button_mul.grid(row=6, column=0)

        button_div = Button(self.root, text="/", command=lambda: self.append_sign("/"))
        button_div.grid(row=6, column=1)

        button_eq = Button(self.root, text="=", command=lambda: self.solve_equation())
        button_eq.grid(row=6, column=2)

        button_clear = Button(self.root, text="Clear", command=lambda: self.clear_equation())
        button_clear.grid(row=1, column=4)

        button_clear = Button(self.root, text="<<<", command=lambda: self.back_on_equation())
        button_clear.grid(row=1, column=5)

        button_pow = Button(self.root, text="^", command=lambda: self.append_sign("^"))
        button_pow.grid(row=2, column=4)

        button_par_left = Button(self.root, text="(", command=lambda: self.append_sign("("))
        button_par_left.grid(row=2, column=5)

        button_pow = Button(self.root, text="!", command=lambda: self.append_sign("!"))
        button_pow.grid(row=3, column=4)

        button_par_right = Button(self.root, text=")", command=lambda: self.append_sign(")"))
        button_par_right.grid(row=3, column=5)

        button_sqrt = Button(self.root, text="sqrt", command=lambda: self.append_sign("sqrt"))
        button_sqrt.grid(row=4, column=4)

        button_abs_left = Button(self.root, text="|", command=lambda: self.append_sign("|"))
        button_abs_left.grid(row=4, column=5)

        button_mod = Button(self.root, text="mod", command=lambda: self.append_sign("mod"))
        button_mod.grid(row=5, column=4)

        button_abs_right = Button(self.root, text="|", command=lambda: self.append_sign("|"))
        button_abs_right.grid(row=5, column=5)

        button_log = Button(self.root, text="log", command=lambda: self.append_sign("log"))
        button_log.grid(row=6, column=4)

        button_dot = Button(self.root, text=".", command=lambda: self.append_sign("."))
        button_dot.grid(row=6, column=5)

    def start_interface(self):
        self.root.mainloop()

    def append_sign(self, sign):
        if not sign.isnumeric() and sign != '.':
            sign = sign+" "
            if len(self.equation_to_display) > 0:
                if self.equation_to_display[-1] != " ":
                    sign = " "+sign

        self.equation_to_display += sign
        self.entry_display.configure(text=self.equation_to_display)
        print(self.equation_to_display)

    def clear_equation(self):
        self.equation_to_display = ""
        self.entry_display.configure(text=self.equation_to_display)
        print(self.equation_to_display)

    def solve_equation(self):
        tree = parse_tree.infix_to_tree(self.equation_to_display)
        result = parse_tree.calculate_equation(tree)
        self.result_display.configure(text=str(result))
        print(self.equation_to_display)

    def back_on_equation(self):
        if self.equation_to_display[-1] == " ":
            self.equation_to_display = self.equation_to_display[:-1]
        self.equation_to_display = self.equation_to_display[:-1]
        self.entry_display.configure(text=self.equation_to_display)