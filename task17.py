import tkinter as tk


def add_two():
    global number
    number += 2
    label.config(text=str(number))


def multiply_by_three():
    global number
    number *= 3
    label.config(text=str(number))


number = 1
root = tk.Tk()
label = tk.Label(root, text=str(number))
label.pack()
tk.Button(root, text="+2", command=add_two).pack()
tk.Button(root, text="×3", command=multiply_by_three).pack()
root.mainloop()
