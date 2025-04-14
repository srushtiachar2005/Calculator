from tkinter import Tk, Entry, Button, StringVar, Frame

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('360x450+100+100')
        master.config(bg='#2C3E50')  # Dark background
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        Entry(master, width=17, bg='#ECF0F1', fg='#2C3E50',
              font=('Helvetica', 26, 'bold'), bd=10,
              insertbackground='#2C3E50', justify='right',
              textvariable=self.equation).place(x=10, y=10)

        button_cfg = {
            'width': 5,
            'height': 2,
            'font': ('Helvetica', 14, 'bold'),
            'relief': 'groove',
            'bd': 2,
            'activebackground': '#AED6F1',
            'cursor': 'hand2'
        }

        # Button layout
        buttons = [
            ('(', 0, 80), (')', 90, 80), ('%', 180, 80), ('/', 270, 80),
            ('1', 0, 150), ('2', 90, 150), ('3', 180, 150), ('*', 270, 150),
            ('4', 0, 220), ('5', 90, 220), ('6', 180, 220), ('-', 270, 220),
            ('7', 0, 290), ('8', 90, 290), ('9', 180, 290), ('+', 270, 290),
            ('C', 0, 360), ('0', 90, 360), ('.', 180, 360), ('=', 270, 360),
        ]

        for (text, x, y) in buttons:
            color = '#ECF0F1'  # light button background
            fg = '#2C3E50'     # dark text

            if text == '=':
                color = '#2ECC71'  # green
                fg = 'white'
                cmd = self.solve
            elif text == 'C':
                color = '#E74C3C'  # red
                fg = 'white'
                cmd = self.clear
            else:
                cmd = lambda val=text: self.show(val)

            Button(master, text=text, bg=color, fg=fg, command=cmd,
                   **button_cfg).place(x=x+10, y=y)

        # === Optional Separators (Thin lines) ===
        for x in [87, 177, 267]:
            Frame(master, bg='#34495E', width=2, height=360).place(x=x+10, y=80)
        for y in [145, 215, 285, 355]:
            Frame(master, bg='#34495E', width=340, height=2).place(x=10, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = str(eval(self.entry_value))
            self.equation.set(result)
            self.entry_value = result
        except:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
