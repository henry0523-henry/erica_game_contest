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
input_index = 0
is_waiting_for_input = False


def start_next_round():
    new_color = choice(colors)
    memory_color.append(new_color)
    show_sequence(0)


def show_sequence(index=0):
    if index < len(memory_color):
        label1.config(bg=memory_color[index])
        tk.after(
            350,
            lambda: (
                label1.config(bg="white"),
                tk.after(100, lambda: show_sequence(index + 1)),
            ),
        )
    else:
        global is_waiting_for_input, input_index
        label1.config(bg="white")
        is_waiting_for_input = True
        input_index = 0


def reset_game():
    global memory_color, is_waiting_for_input, input_index
    memory_color.clear()
    is_waiting_for_input = False
    input_index = 0
    tk.after(500, start_next_round)


def button_click(color):
    global input_index, is_waiting_for_input
    if not is_waiting_for_input:
        return
    expected_color = memory_color[input_index]
    if color == expected_color:
        input_index += 1
        if input_index == len(memory_color):
            is_waiting_for_input = False
            tk.after(100, start_next_round)
    else:
        is_waiting_for_input = False
        tk.after(0, tk.destroy)


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

tk.after(300, start_next_round)


tk.mainloop()

print(f"""your score: {len(memory_color) - 1}""")