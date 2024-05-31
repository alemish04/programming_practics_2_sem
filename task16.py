import tkinter as tk

root = tk.Tk()
for i in range(8):
    for j in range(8):
        color = "white" if (i + j) % 2 == 0 else "black"
        tk.Button(root, width=2, height=1, bg=color).grid(row=i, column=j)
root.mainloop()
