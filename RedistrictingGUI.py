import tkinter as tk
from tkinter import ttk

import RedistrictingProject as RP


window = tk.Tk()
window.title('Redistricting Calculator')
window.geometry("800x800")
window.configure(bg='white')
window.resizable(width=True, height=True)

frame = tk.Frame(window, bg='#0052cc')
frame.place(relx=.1, rely=.1, relwidth=0.8, relheight=0.8)

# for i in range(10):
#     frame.columnconfigure(i, weight=1)

# def visblock():
#     icon = PhotoImage(file="Player_Icon.png")
#     block = tk.Label(window, image=icon)
#     return block
# # These act like walls

# def invisblock():
#     icon = PhotoImage(file="Player_Icon_Cover.png")
#     block = tk.Button(window, image=icon)
#     return block
# # These act like empty spaces"""

# maze = [[visblock(), visblock(), visblock(), visblock()],
#         [visblock(), invisblock(), invisblock(), visblock()],
#         [invisblock(), invisblock(),visblock(), invisblock()],
#         [visblock(), invisblock(), invisblock(), invisblock()],
#         [visblock(),visblock(), visblock(), visblock()]]

for i, block_row in enumerate(RP.Squareville):
    for j, block in enumerate(block_row):
        label = ttk.Label(window, text=block)
        label.grid(row=i, column=j)
        pass


window.mainloop()