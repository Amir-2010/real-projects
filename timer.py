
# let's make one digital clock!
from tkinter import *
from time import strftime

def clock_func():
    clock_var = strftime(" %H : %M : %S %p ")
    label_clock.config(text=clock_var)
    label_clock.after(1000,clock_func)

window = Tk()
window.resizable(False,False)
window.title("Clock")

img = PhotoImage(file="E:/Images/Clock.png")
window.iconphoto(True,img)

label_clock = Label(window,
                    font=("ds-digital",80), # for make the numbers and characters you have to install this font
                    background="black",
                    foreground="Cyan",
                    height=2)
label_clock.pack(fill="x",anchor="center")

clock_func()
window.mainloop()
