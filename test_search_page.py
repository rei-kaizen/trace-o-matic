import csv
from tkinter import *

class SearchWindow:
    def __init__(self, parent):
        self.parent = parent
        self.top = Toplevel(parent)
        self.top.geometry("300x200")
        self.top.title('Search Results')
        
        self.userdata = self.read_csv_data("entries.csv")

        self.entry = Entry(self.top)
        self.entry.pack()
        self.entry.bind('<KeyRelease>', self.scan_key)

        self.listbox = Listbox(self.top)
        self.listbox.pack()
        self.listbox.bind('<Double-Button-1>', self.show_user_info)

        self.info_label = Label(self.top, text="", justify=LEFT)
        self.info_label.pack()

        self.update(self.userdata)

    def read_csv_data(self, filename):
        data = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def scan_key(self, event):
        val = self.entry.get()
        if val == '':
            data = self.userdata
        else:
            data = []
            for user in self.userdata:
                if any(val.lower() in str(item).lower() for item in user):
                    data.append(user)
        self.update(data)

    def update(self, data):
        self.listbox.delete(0, 'end')
        for user in data:
            self.listbox.insert('end', user[0])  # Display the name (column 1)

    def show_user_info(self, event):
        selected_user_index = self.listbox.curselection()
        if selected_user_index:
            user_info = self.userdata[selected_user_index[0]]
            self.show_info(user_info)

    def show_info(self, user_info):
        self.info_label.config(text=f"Gender: {user_info[1]}\n"
                                f"Address: {user_info[2]}\n"
                                f"Civil Status: {user_info[3]}\n"
                                f"Birthday: {user_info[4]}\n"
                                f"Phone Number: {user_info[5]}\n"
                                f"Landline: {user_info[6]}")

if __name__ == "__main__":
    ws = Tk()
    app = SearchWindow(ws)
    ws.mainloop()
