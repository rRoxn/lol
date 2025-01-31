import tkinter as tk

window = tk.Tk()

def killWindow():

    window.destroy()

for i in range (4):

    window.columnconfigure(i, weight = 10, minsize = 100)

    window.rowconfigure(i, weight = 10, minsize = 75)

    for j in range(3):

        etikett = tk.Label(

            master = window,

            relief = tk.RAISED,

            borderwidth = 3,

            text = "Rad {} \nKolumn {}".format(i, j)

            )

        etikett.grid(

            row = i,

            column = j,

            padx = 5,

            pady = 5

            )

buttonQuit = tk.Button(

    text = "Avsluta",

    width = 10,

    height = 3,

    command = killWindow

    )

buttonQuit.grid(

    row = 5,

    column = 1

    )

window.columnconfigure(1, weight = 10, minsize = 100)

window.rowconfigure(5, weight = 10, minsize = 75)

window.mainloop()