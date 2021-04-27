import sqlite3
import tkinter
import tkinter.messagebox as mb


class MyMainTkinterWindow:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x500")
        self.root.title("Hello World GUI")

        # CREATE INDEX FOR OUR RETURNED DATA SET
        self.var_recordset_index = tkinter.IntVar(self.root)
        self.var_recordset_index.set(0)
        self.var_rowcount = tkinter.IntVar(self.root)

        self.var_book_id = tkinter.StringVar(self.root)
        self.var_title = tkinter.StringVar(self.root)
        self.var_genre = tkinter.StringVar(self.root)
        self.var_published_date = tkinter.StringVar(self.root)

        self.book_window_label = tkinter.Label(self.root, text="Library System: BOOKS")
        self.book_window_label.grid(row=0, column=0, columnspan=2)
        self.book_id = tkinter.Label(self.root, text="Book ID:")
        self.book_id.grid(padx=20, pady=20, row=1, column=0)
        self.book_id_entry = tkinter.Entry(self.root, textvariable=self.var_book_id, bd=3)
        self.book_id_entry.grid(padx=20, pady=20, row=1, column=1)
        self.title = tkinter.Label(self.root, text="Title:")
        self.title.grid(padx=20, pady=20, row=2, column=0)
        self.title_entry = tkinter.Entry(self.root, textvariable=self.var_title, bd=3)
        self.title_entry.grid(padx=20, pady=20, row=2, column=1)
        self.genre = tkinter.Label(self.root, text="Genre:")
        self.genre.grid(padx=20, pady=20, row=3, column=0)
        self.genre_entry = tkinter.Entry(self.root, textvariable=self.var_genre, bd=3)
        self.genre_entry.grid(padx=20, pady=20, row=3, column=1)
        self.published_date = tkinter.Label(self.root, text="Published Date:")
        self.published_date.grid(padx=20, pady=20, row=4, column=0)
        self.published_date_entry = tkinter.Entry(self.root, textvariable=self.var_published_date, bd=3)
        self.published_date_entry.grid(padx=20, pady=20, row=4, column=1)

        self.nav_backward_btn = tkinter.Button(self.root, text="<", command=self.nav_backward)
        self.nav_backward_btn.grid(row=6, column=0)
        self.nav_forward_btn = tkinter.Button(self.root, text=">", command=self.nav_forward)
        self.nav_forward_btn.grid(row=6, column=3)

        self.insert_btn = tkinter.Button(self.root, text="INSERT", command=self.insert, state="disabled")
        self.insert_btn.grid(row=7, column=0)
        self.update_btn = tkinter.Button(self.root, text="UPDATE", command=self.update)
        self.update_btn.grid(row=7, column=1)
        self.delete_btn = tkinter.Button(self.root, text="DELETE", command=self.delete)
        self.delete_btn.grid(row=7, column=2)
        self.new_btn = tkinter.Button(self.root, text="NEW", command=self.new)
        self.new_btn.grid(row=7, column=3)

    def nav_forward(self):
        print("Nav Forward")
        self.var_recordset_index.set(self.var_recordset_index.get() + 1)
        self.set_data()

    def nav_backward(self):
        print("Nav backward")
        self.var_recordset_index.set(self.var_recordset_index.get() - 1)
        self.set_data()

    def set_data(self):
        data = self.load_books()
        row = data[self.var_recordset_index.get()]
        self.var_book_id.set(row[0])  # ID
        self.var_title.set(row[1])
        self.var_genre.set(row[2])
        self.var_published_date.set(row[3])

    def load_books(self):
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        c.execute("SELECT * FROM books")
        data = c.fetchall()
        #self.root.var_rowcount.set(c.rowcount)
        row = data[0]
        print(row[1])
        return data

    def insert(self):
        print("INSERT")
        book = [self.var_title.get(), self.var_genre.get(), self.var_published_date.get()]
        insert_query = "INSERT INTO books VALUES (null,?,?,?)"
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        c.execute(insert_query, book)
        conn.commit()
        self.set_data()
        self.insert_btn["state"] = "disabled"

    def update(self):
        print("UPDATE")
        book = [self.var_title.get(), self.var_genre.get(), self.var_published_date.get(),
                self.var_book_id.get()]
        update_query = "UPDATE books SET title=? , genre=?, published_date= ? WHERE book_id=?"
        conn = sqlite3.connect('library.db')
        c = conn.cursor()
        c.execute(update_query, book)
        conn.commit()
        self.set_data()

    def new(self):
        self.var_title.set("")
        self.var_genre.set("")
        self.var_published_date.set("")
        self.var_book_id.set("")
        self.insert_btn["state"] = "active"
        print("NEW")

    def delete(self):
        MsgBox = mb.askquestion('DELETE RECORD',
                                                'Are you sure you want to delete the current record? This cannot be undone.',
                                                icon='warning')
        if MsgBox == 'yes':
            conn = sqlite3.connect('library.db')
            c = conn.cursor()
            delete_query = "DELETE FROM books WHERE book_id=" + str(self.var_book_id.get())
            print(delete_query)
            c.execute(delete_query)
            conn.commit()
            self.set_data()

        print("DELETED")


if __name__ == "__main__":
    myApp = MyMainTkinterWindow()
    myApp.set_data()
    myApp.root.mainloop()
