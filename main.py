import sqlite3
from tkinter import *


def load_books():
    table = "books"
    conn = sqlite3.connect('library.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()
    print("###### Getting all data from ", table, " ######")
    query = "SELECT * FROM " + table
    print(query)
    c.execute(query)
    data = c.fetchone()
    print(data)
    var_book_id.set(data[0])
    var_title.set(data[1])
    var_genre.set(data[2])
    var_published_date.set(data[3])
    conn.close()


root = Tk()
root.geometry("500x500")
root.title("Hello World GUI")

var_book_id = StringVar(root)
var_title = StringVar(root)
var_genre = StringVar(root)
var_published_date = StringVar(root)

book_window_label = Label(root, text="Library System: BOOKS")
book_window_label.grid(row=0, column=0, columnspan=2)
book_id = Label(root, text="Book ID:")
book_id.grid(padx=20, pady=20, row=1, column=0)
book_id_entry = Entry(root, textvariable=var_book_id, bd=3)
book_id_entry.grid(padx=20, pady=20, row=1, column=1)
title = Label(root, text="Title:")
title.grid(padx=20, pady=20, row=2, column=0)
title_entry = Entry(root, textvariable=var_title, bd=3)
title_entry.grid(padx=20, pady=20, row=2, column=1)
genre = Label(root, text="Genre:")
genre.grid(padx=20, pady=20, row=3, column=0)
genre_entry = Entry(root, textvariable=var_genre, bd=3)
genre_entry.grid(padx=20, pady=20, row=3, column=1)
published_date = Label(root, text="Published Date:")
published_date.grid(padx=20, pady=20, row=4, column=0)
published_date_entry = Entry(root, textvariable=var_published_date, bd=3)
published_date_entry.grid(padx=20, pady=20, row=4, column=1)
save_btn = Button(root, text="Load Books", command=load_books)
save_btn.grid(row=6, column=3)
root.mainloop()
