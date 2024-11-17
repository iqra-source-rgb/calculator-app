import tkinter as tk

def click(event):
    global equation
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(equation.get()))
            equation.set(result)
        except Exception as e:
            equation.set("Error")
    elif text == "C":
        equation.set("")
    else:
        equation.set(equation.get() + text)

# Create GUI window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Variable to hold the equation
equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=8, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 0, 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font=("Arial", 18), relief=tk.RAISED, bd=2, height=2, width=4)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
