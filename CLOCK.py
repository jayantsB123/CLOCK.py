import tkinter
from time import strftime
def tym():
    t= strftime("%H:%M:%S %p")
    lbl.config(text=t)
    lbl.pack()
    lbl.after(1000, tym)
    temp= f"Current time is: {t}"
    # print(temp)
    # print(t)
    pass
clock = tkinter.Tk()

lbl=tkinter.Label(clock)
lbl = tkinter.Label(clock, background="black", foreground="red", font=("Comic Sans MS",55,"bold"))
lbl_2 = tkinter.Label(clock, text="Time is:")
lbl_2.pack()


tym()
clock.mainloop()
