import tkinter as tk
root = tk.Tk()
root.geometry("600x300")
root.title("My First TKinter Project")

label1=tk.Label(root,text="Hello Rutuja")
label2=tk.Label(root,text="This is Our First Page")
label1.pack()
label2.pack()

def hi():
    print("Hello Rutuja")
btn = tk.Button(root, text="Click Me", bg="blue", fg="white", command=hi, width=10, font=("Arial",10)).pack(side="bottom")


entry = tk.Entry(root, bg="lightblue")
entry.insert(0, "Enter Your Name: ")
entry.pack()
def getData():
    print(entry.get())
btn2 = tk.Button(root, text="Get Data", bg="green", fg="white", command=getData, width=5, font=("Arial",10)).pack(side="bottom")

root.mainloop()