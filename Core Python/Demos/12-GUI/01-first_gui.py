import tkinter as tk
root = tk.Tk()
root.geometry("600x300")
root.title("My First TKinter Project")

label1=tk.Label(root,text="Hello Rutuja")
label2=tk.Label(root,text="This is Our First Page")
label1.pack()
label2.pack()

root.mainloop()