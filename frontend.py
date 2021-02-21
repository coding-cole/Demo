from tkinter import *
import backend


def get_selected_row(event):
    global selected_turple
    index = list1.curselection()[0]
    selected_turple = list1.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_turple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_turple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_turple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_turple[4])


def view_command():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),
                       year_text.get(), isbn_text.get()))


def delete_command():
    backend.delete(selected_turple[0])


def update_command():
    backend.update(selected_turple[0], title_text.get(
    ), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()
window.wm_title("Bookstore")
# labels
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

# entries
title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

# list
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# scrollbar
scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)

# connecting the scroll bar to listbox
list1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

# buttons
button1 = Button(window, text="View All", width=12, command=view_command)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search entry", width=12, command=search_command)
button2.grid(row=3, column=3)

button3 = Button(window, text="Add entry", width=12, command=add_command)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update selected",
                 width=12, command=update_command)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete selected",
                 width=12, command=delete_command)
button5.grid(row=6, column=3)

button6 = Button(window, text="Close", width=12, command=window.destroy)
button6.grid(row=7, column=3)


window.mainloop()
