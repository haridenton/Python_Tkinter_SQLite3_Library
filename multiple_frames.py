import tkinter as tk             # This has all the code for GUIs.
import tkinter.font as font      # This lets us use different fonts.


def center_window_on_screen():
    x_cord = int((screen_width/2) - (width/2))
    y_cord = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


def change_to_work():
    red_frame.forget()
    blue_frame.pack(fill='both', expand=1)


def change_to_quiz():
    red_frame.pack(fill='both', expand=1)
    blue_frame.forget()


root = tk.Tk()
root.title("Multiple Frames - Swapping frames")
root.configure(bg='lightyellow')
width, height = 500, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_window_on_screen()

# Here, we create two frames of which only
# one will be visible at a time.
red_frame = tk.Frame(root, bg="red")
blue_frame = tk.Frame(root, bg="blue")

# Let's create the fonts that we need.
font_large = font.Font(family='Georgia',  size='24',  weight='bold')
font_small = font.Font(family='Georgia',  size='12')

lbl_heading_red = tk.Label(red_frame, text='This is the RED frame', font=font_large)

lbl_heading_red.pack(pady=20)
btn_change_to_blue = tk.Button(red_frame, text='Change to BLUE', font=font_small, command=change_to_work)
btn_change_to_blue.pack(pady=20)

lbl_heading_blue = tk.Label(blue_frame, text='This is the BLUE frame', font=font_large)
lbl_heading_blue.pack(pady=20)
btn_change_to_red = tk.Button(blue_frame, font=font_small, text='Change to RED', command=change_to_quiz)
btn_change_to_red.pack(pady=20)

red_frame.pack(fill='both', expand=1)
root.mainloop()