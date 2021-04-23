import sqlite3
from tkinter import *
from tkinter import messagebox



def nav_forward():
    print("Nav Forward")
    var_recordset_index.set(var_recordset_index.get() + 1)
    set_data()


def nav_backward():
    print("Nav backward")
    var_recordset_index.set(var_recordset_index.get() - 1)
    set_data()


def load_books():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    data = c.fetchall()
    var_rowcount.set(c.rowcount)
    row = data[0]
    print(row[1])
    return data


def set_data():
    data = load_books()
    row = data[var_recordset_index.get()]
    var_book_id.set(row[0])  # ID
    var_title.set(row[1])
    var_genre.set(row[2])
    var_published_date.set(row[3])


def insert():
    print("INSERT")
    book = [var_title.get(), var_genre.get(), var_published_date.get()]
    insert_query = "INSERT INTO books VALUES (null,?,?,?)"
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute(insert_query, book)
    conn.commit()
    set_data()
    insert_btn["state"] = "disabled"


def update():
    print("UPDATE")
    book = [var_title.get(), var_genre.get(), var_published_date.get(), var_book_id.get()]
    update_query = "UPDATE books SET title=? , genre=?, published_date= ? WHERE book_id=?"
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute(update_query, book)
    conn.commit()
    set_data()


def new():
    var_title.set("")
    var_genre.set("")
    var_published_date.set("")
    var_book_id.set("")
    insert_btn["state"] = "active"
    print("NEW")


def delete():
    MsgBox = messagebox.askquestion('DELETE RECORD',
                                    'Are you sure you want to delete the current record? This cannot be undone.',
                                    icon='warning')
    if MsgBox == 'yes':
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        delete_query = "DELETE FROM books WHERE book_id=" + str(var_book_id.get())
        print(delete_query)
        c.execute(delete_query)
        conn.commit()
        set_data()

    print("DELETED")


root = Tk()
root.geometry("500x500")
root.title("Hello World GUI")

# CREATE INDEX FOR OUR RETURNED DATA SET
var_recordset_index = IntVar()
var_recordset_index.set(0)
var_rowcount = IntVar()

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

nav_backward_btn = Button(root, text="<", command=nav_backward)
nav_backward_btn.grid(row=6, column=0)
nav_forward_btn = Button(root, text=">", command=nav_forward)
nav_forward_btn.grid(row=6, column=3)

insert_btn = Button(root, text="INSERT", command=insert, state="disabled")
insert_btn.grid(row=7, column=0)
update_btn = Button(root, text="UPDATE", command=update)
update_btn.grid(row=7, column=1)
delete_btn = Button(root, text="DELETE", command=delete)
delete_btn.grid(row=7, column=2)
new_btn = Button(root, text="NEW", command=new)
new_btn.grid(row=7, column=3)

set_data()
root.mainloop()
