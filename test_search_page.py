import csv
from tkinter import *

def read_csv_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def scan_key(event):
    val = event.widget.get()
    if val == '':
        data = userdata
    else:
        data = []
        for user in userdata:
            if any(val.lower() in str(item).lower() for item in user):
                data.append(user)
    update(data)

def update(data):
    listbox.delete(0, 'end')
    for user in data:
        listbox.insert('end', user[0])  # Display the name (column 1)

def show_user_info(event):
    selected_user_index = listbox.curselection()
    if selected_user_index:
        user_info = userdata[selected_user_index[0]]
        show_info(user_info)

def show_info(user_info):
    info_label.config(text=f"Gender: {user_info[1]}\n"
                            f"Address: {user_info[2]}\n"
                            f"Civil Status: {user_info[3]}\n"
                            f"Birthday: {user_info[4]}\n"
                            f"Phone Number: {user_info[5]}\n"
                            f"Landline: {user_info[6]}")

userdata = read_csv_data("entries.csv")

ws = Tk()

entry = Entry(ws)
entry.pack()
entry.bind('<KeyRelease>', scan_key)

listbox = Listbox(ws)
listbox.pack()
listbox.bind('<Double-Button-1>', show_user_info)

info_label = Label(ws, text="", justify=LEFT)
info_label.pack()

update(userdata)

ws.mainloop()
