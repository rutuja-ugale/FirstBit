import tkinter as tk
root=tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")
root.config(bg="gray")
display=tk.Entry(root, font=("Cursive", 20), bg="white", fg="black", bd=5,relief="sunken", justify="right")
display.pack(pady=20, padx=20, fill="x")

def click(values):
    display.insert(tk.END, values)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
frame = tk.Frame(root, bg="red")
frame.pack()
buttons = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("+", 3, 2),
    # ("=", 3, 3),
]
for text,row,column in buttons:
    if text in "+-*/":
        color="orange"
    else:
        color="lightgray"
    tk.Button(frame, text=text, font=("Cursive", 20, "bold"),bg=color,fg="white", command=lambda t=text: click(x)).grid(row=row, column=column)
tk.Button(
    frame, text="C", font=("Cursive", 20, "bold"), bg="red", fg="white", command=clear
)
root.mainloop()
