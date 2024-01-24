from tkinter import Tk, Entry, Button, StringVar

class Calc:
    def __init__(self, master):
        # Set up the calculator window
        master.title('Calculator')
        master.geometry('357x420+0+0')
        master.config(bg='black')
        master.resizable(False, False)

        # Initialize variables for equation and entry value
        self.equation = StringVar()
        self.entry_val = ''

        # Create Entry widget for displaying the equation
        Entry(width=17, bg='#ff9595', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Line 1: Create buttons for '(', ')', '%', '/'
        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)

        # Line 2: Create buttons for '1', '2', '3', '*'
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show('1')).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show('2')).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show('3')).place(x=180, y=125)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)

        # Line 3: Create buttons for '4', '5', '6', '-'
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show('4')).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show('5')).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show('6')).place(x=180, y=200)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=200)

        # Line 4: Create buttons for '7', '8', '9', '+'
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show('7')).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show('8')).place(x=90, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show('9')).place(x=180, y=275)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=275)

        # Line 5: Create buttons for 'C', '0', '.', '='
        Button(width=11, height=4, text='C', relief='flat', bg='#bcbcbc', command=lambda: self.clear()).place(x=0, y=350)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command=lambda: self.solver()).place(x=270, y=350)

    def show(self, VAL):
        # Update entry value and displayed equation
        self.entry_val += str(VAL)
        self.equation.set(self.entry_val)

    def clear(self):
        # Clear entry value and displayed equation
        self.entry_val = ''
        self.equation.set(self.entry_val)

    def solver(self):
        # Evaluate the expression and update the displayed equation with the result
        result = eval(self.entry_val)
        self.equation.set(result)

# Create the main Tkinter window and calculator instance
root = Tk()
Calc = Calc(root)

# Start the Tkinter event loop
root.mainloop()
