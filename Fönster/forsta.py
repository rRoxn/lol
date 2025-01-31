import tkinter as tk

window = tk.Tk()

def fixColor():

    if etikett.cget("bg") == "yellow":

        etikett.config(bg = "red")

    else:

        etikett.config(bg = "yellow")

def fixText():

    etikett.config(text = nyText.get())

etikett = tk.Label(

    text = "Hejsan alla glada!",

    width = 20,

    height = 20,

    foreground = "blue",

    background = "red"

    )

nyText = tk.Entry(

    width = 50

    )

 

buttonColor = tk.Button(

    text = "Ändra färg!",

    width = 25,

    height = 5,

    command = fixColor

    )

buttonText = tk.Button(

    text = "Ändra text",

    width = 25,

    height = 5,

    command = fixText

    )

etikett.pack()

nyText.pack()

buttonColor.pack()

buttonText.pack()

 

window.mainloop()