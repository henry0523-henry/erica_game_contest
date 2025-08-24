from tkinter import *
from random import choice

tk = Tk()
buttons = [[None for _ in range(3)] for _ in range(3)]

label1 = Label(
    tk,
    width=14,
    height=7,
    bg="white",
    fg="white",
    relief="flat",
    font=("Arial", 12),
)

colors = ["red", "blue", "green", "yellow", "orange", "pink", "brown", "gray"]
color_index = 0

memory_color = []

def button_click(color):
    print(color)

for row in range(3):
    for col in range(3):
        if row == 1 and col == 1:
            label1.grid(row=row, column=col)
            buttons[row][col] = label1
        else:
            current_color = colors[color_index % len(colors)]
            btn = Button(
                tk,
                width=14,
                height=7,
                bg=current_color,
                activebackground=current_color,
                font=("Arial", 12),
                command=lambda color=current_color: button_click(color),
            )
            btn.grid(row=row, column=col)
            buttons[row][col] = btn
            color_index += 1

tk.mainloop()
