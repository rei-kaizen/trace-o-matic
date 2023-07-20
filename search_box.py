import csv
from tkinter import *
from ttkbootstrap import *
from info_display import OutputWindow 

class SearchWindow:
    def __init__(self, parent):
        self.parent = parent
        self.top = Toplevel(parent)
        self.top.geometry("160x230")
        self.top.title('Search Entries')
        
        self.userdata = self.read_csv_data("test_entries.csv")

        self.entry = Entry(self.top)
        self.entry.pack(padx=5, pady=5)
        self.entry.insert(0, "\U0001F50D Search Names")
        self.entry.bind("<FocusIn>", self.fadein)
        self.entry.bind('<KeyRelease>', self.scan_key)

        self.listbox = Listbox(self.top, height=10)
        self.listbox.pack()
        self.listbox.bind('<Double-Button-1>', self.show_user_info)

        self.info_label = Label(self.top, text="", justify=LEFT)
        self.info_label.pack(pady=1)

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
            self.listbox.insert('end', user[0])
    
    def show_user_info(self, event):
        selected_user_index = self.listbox.curselection()
        if selected_user_index:
            user_info = self.userdata[selected_user_index[0]]
            OutputWindow(self.top, user_info)

    
    def fadein(self, event):
        self.entry.delete(0, END)
    
if __name__ == "__main__":
    ws = Tk()
    app = SearchWindow(ws)
    ws.mainloop()
