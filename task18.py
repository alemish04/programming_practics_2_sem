import tkinter as tk


def move(event):
    x, y = button.winfo_x(), button.winfo_y()
    if event.char == 'w':
        y -= 10
    elif event.char == 'a':
        x -= 10
    elif event.char == 's':
        y += 10
    elif event.char == 'd':
        x += 10
    button.place(x=x, y=y)


root = tk.Tk()
button = tk.Button(root, text="Button")
button.place(x=50, y=50)
root.bind("<Key>", move)
root.mainloop()
