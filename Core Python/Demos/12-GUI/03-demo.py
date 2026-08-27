import tkinter as tk
r = tk.Tk()
r.geometry("600x300")
r.title("My TKinter Project")
l1=tk.Label(r,text="Welcome", bg="orange", fg="black", font=12).grid(row=1,column=1)

entr=tk.Entry(r, bg="lightblue", font=("arial", 12), width=20, justify="center")
entr.grid(row=2,column=1, padx=10, pady=10)

def getdata():
    l2=tk.Label(r,text="Your Data is: "+entr.get(),bg="lightgray",fg="blue", font=10).grid(row=3, column=1)

btn=tk.Button(r,text="Get Data", bg="green", fg="white", command=getdata, font=("arial", 12)).grid(row=2, column=2)


# Create CheckBox

ch=tk.Checkbutton(r,text="I Agree", bg="lightblue", fg="black", font=10).grid(row=4, column=1)
ch1=tk.Checkbutton(r,text="I Agree", bg="lightblue", fg="black", font=10).grid(row=5, column=1)
ch2=tk.Checkbutton(r,text="I Agree", bg="lightblue", fg="black", font=10).grid(row=6, column=1)

def getData():
    print(ch1.get())
bt=tk.Button(r,text="Click me", command=getData, bg="yellow").grid(row=3, column=4)
r.mainloop()