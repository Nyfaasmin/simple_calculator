from tkinter import *

strng = ""

def click(n):
    global strng
    strng += str(n)
    eq.set(strng)

def equalto():
    try:
        global strng
        result = str(eval(strng))
        eq.set(result)
        strng = ""
    except:
        eq.set(" Invalid ")
        strng = ""

def clear():
    global strng
    strng = ""
    eq.set("")

def backspace():
    global strng
    if strng:
        strng = strng[:-1]
        eq.set(strng)

def close():
    gui.destroy()

if __name__ == "__main__":
    gui = Tk()
    gui.title("Simple Calculator")
    gui.configure(bg="black")

    # **Set Fixed Window Size**
    gui.geometry("595x575")  # Adjusted to fit buttons properly
    gui.resizable(False, False)  # Prevent resizing

    eq = StringVar()

    # **Entry Field**
    exp_f = Entry(gui, textvariable=eq, font=("Arial", 24), bd=10, relief=SUNKEN, justify=RIGHT)
    exp_f.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, sticky="nsew")

    # **Button Layout**
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
        ('←', 5, 0), ('=', 5, 3)
    ]

    for (text, row, col) in buttons:
        Button(gui, text=text, fg="black", bg="white", font=("Arial", 20),
               command=(lambda t=text: click(t) if t not in ('C', '=', '←') else (
                   clear() if t == 'C' else equalto() if t == '=' else backspace())),
               height=2, width=8).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    # **Exit Button**
    Button(gui, text="Exit", fg="white", bg="red", font=("Arial", 20, "bold"), command=close,
           height=2, width=8).grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")

    gui.mainloop()
