from tkinter import *


def new_window():
    second_window = Toplevel(root)
    second_window.title("NEW WINDOW")
    second_window.geometry("200x200")
    btn_back = Button(second_window, text="BACK", command=lambda: second_window.destroy())
    btn_back.pack()


root = Tk()
root.geometry("400x200")
root.title("Test app")
btn_move = Button(root, text="NEW WINDOW", command=new_window)
btn_move.pack()
root.mainloop()
