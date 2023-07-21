import csv
import tkinter as tk
from info_display import OutputWindow 

class SearchWindow:
    WINDOW_WIDTH = 160
    WINDOW_HEIGHT = 230

    def __init__(self, parent):
        self.parent = parent
        self.top = tk.Toplevel(parent)
        self.top.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.top.title('Search Entries')
        
        self.user_data = self.read_csv_data("test_entries.csv")

        self.create_search_input()
        self.create_user_listbox()
        self.create_info_label()

        self.update_user_listbox(self.user_data)

    def read_csv_data(self, filename):
        data = []
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def create_search_input(self):
        self.search_entry = tk.Entry(self.top)
        self.search_entry.pack(padx=5, pady=5)
        self.search_entry.insert(0, "\U0001F50D Search Names")
        self.search_entry.bind("<FocusIn>", self.fade_in)
        self.search_entry.bind('<KeyRelease>', self.scan_key)

    def create_user_listbox(self):
        self.user_listbox = tk.Listbox(self.top, height=10)
        self.user_listbox.pack()
        self.user_listbox.bind('<Double-Button-1>', self.show_user_info)

    def create_info_label(self):
        self.info_label = tk.Label(self.top, text="", justify=tk.LEFT)
        self.info_label.pack(pady=1)

    def update_user_listbox(self, user_data):
        self.user_listbox.delete(0, 'end')
        for user in user_data:
            self.user_listbox.insert('end', user[0])

    def scan_key(self, event):
        val = self.search_entry.get()
        if val == '':
            data = self.user_data
        else:
            data = []
            for user in self.user_data:
                if any(val.lower() in str(item).lower() for item in user):
                    data.append(user)
        self.update_user_listbox(data)

    def show_user_info(self, event):
        selected_user_index = self.user_listbox.curselection()
        if selected_user_index:
            user_info = self.user_data[selected_user_index[0]]
            OutputWindow(self.top, user_info)

    def fade_in(self, event):
        self.search_entry.delete(0, tk.END)
