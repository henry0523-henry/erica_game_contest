from tkinter import *
from random import choice

tk = Tk()
buttons = [[None for _ in range(3)] for _ in range(3)]

label1 = Label(
    tk,
    text="hi",
    width=14,
    height=7,
    bg="white",
    fg="white",
    relief="flat",
    font=("Arial", 12),
)

colors = ["red", "blue", "green", "yellow", "orange", "pink", "brown", "gray"]
color_index = 0

for row in range(3):
    for col in range(3):
        if row == 1 and col == 1:
            label1.grid(row=row, column=col)
            buttons[row][col] = label1
        else:
            btn = Button(
                tk,
                width=14,
                height=7,
                bg=colors[color_index % len(colors)],
                activebackground=colors[color_index % len(colors)],
                font=("Arial", 12),
                command=lambda r=row, c=col: print(f"Button {r}, {c} clicked")
            )
            btn.grid(row=row, column=col)
            buttons[row][col] = btn
            color_index += 1


print("hi")





tk.mainloop()




