import tkinter as tk             # This has all the code for GUIs.
import tkinter.font as font      # This lets us use different fonts.


def center_window_on_screen():
    x_cord = int((screen_width/2) - (width/2))
    y_cord = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


def change_to_work():
    quiz_frame.forget()
    work_frame.pack(fill='both', expand=1)


def change_to_quiz():
    quiz_frame.pack(fill='both', expand=1)
    work_frame.forget()


root = tk.Tk()
root.title("My Work - Swapping frames")
root.configure(bg='lightyellow')
width, height = 500, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_window_on_screen()

# Here, we create two frames of which only
# one will be visible at a time.
quiz_frame = tk.Frame(root, bg="red")
work_frame = tk.Frame(root, bg="blue")

# Let's create the fonts that we need.
font_large = font.Font(family='Georgia',  size='24',  weight='bold')
font_small = font.Font(family='Georgia',  size='12')

lbl_heading_quiz = tk.Label(quiz_frame, text='This is the quiz frame', font=font_large)

lbl_heading_quiz.pack(pady=20)
btn_change_to_work = tk.Button(quiz_frame, text='Change to work', font=font_small, command=change_to_work)
btn_change_to_work.pack(pady=20)

lbl_heading_work = tk.Label(work_frame, text='This is the WORK frame', font=font_large)
lbl_heading_work.pack(pady=20)
btn_change_to_quiz = tk.Button(work_frame, font=font_small, text='Change to quiz', command=change_to_quiz)
btn_change_to_quiz.pack(pady=20)

quiz_frame.pack(fill='both', expand=1)
root.mainloop()