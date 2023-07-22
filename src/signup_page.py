from tkinter import *
import tkinter.ttk as ttk
import ttkbootstrap as tb
from consent_form import DataPrivacy
import csv

class SignUpWindow:
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 600
    GENDER_VALUES = ["Female", "Male"]
    CS_VALUES = ["Annuled", "Cohabiting", "Divorce", "Not Specified", "Married", "Separated", "Single", "Widowed"]

    def __init__(self, home_page):
        self.home_page = home_page
        self.win1 = Toplevel(home_page)

        self.window_properties()
        self.banner()
        self.set_input_fields()
        self.buttons()

        self.win1.mainloop()

    def window_properties(self):
        self.win1.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.win1.title('Registration')
           
    def banner(self):
        heading_label = Label(self.win1, text="Sign Up", font=("Arial Rounded MT Bold", 20))
        heading_label.place(x=20, y=10)

        subheading_label = Label(self.win1, text="Enter your details to create your entry", font=("Cobrel", 11), fg="gray")
        subheading_label.place(x=20, y=50)

    def set_input_fields(self):
        self.name_entry = self.input_fields("Full Name", 20, 100, 40)
        self.gender_combo = self.combobox("Gender", self.GENDER_VALUES, 300, 100)
        self.address_entry = self.input_fields("Address", 20, 170, 40)
        self.cs_combo = self.combobox("Civil Status", self.CS_VALUES, 300, 170)
        self.email_entry = self.input_fields("Email", 20, 240, 40)
        self.datetime = self.calendar(300, 240)
        self.cp_entry = self.input_fields("Phone Number", 20, 310, 40)

    def buttons(self):
        agree = Checkbutton(self.win1, text="I Agree to", font=("Corbel", 10), activebackground="#39767A")
        agree.place(x=20, y=375)

        consent = tb.Button(self.win1, text="Data Privacy Consent.", bootstyle="light", command=self.consent)
        consent.place(x=100, y=375)
    
        submit = tb.Button(self.win1, text="Submit",  bootstyle="info", command=self.submit)
        submit.place(x=20, y=420)

        cancel = tb.Button(self.win1, text="Cancel", bootstyle="info-outline", command=self.close_window)
        cancel.place(x=100, y=420)

    def input_fields(self, label_text, x_pos, y_pos, width):
        label = Label(self.win1, text=label_text, font=("Corbel", 10), fg="black")
        label.place(x=x_pos, y=y_pos)

        entry = Entry(self.win1, font=("Corbel", 9), fg="black", width=width, bd=1, bg="#E8E6E5")
        entry.place(x=x_pos, y=y_pos+20)

        return entry

    def combobox(self, label_text, values, x_pos, y_pos):
        label = Label(self.win1, text=label_text, font=("Corbel", 10), fg="black")
        label.place(x=x_pos, y=y_pos)

        combo = ttk.Combobox(self.win1, values=values, font=("Corbel", 10))
        combo.place(x=x_pos, y=y_pos+20)

        return combo

    def calendar(self, x_pos, y_pos):
        calendar = tb.DateEntry(self.win1)
        calendar.place(x=x_pos, y=y_pos)

        return calendar
        
    def close_window(self):
        self.win1.destroy()
        self.home_page.deiconify()

    def consent(self):
        DataPrivacy(self.win1)

    def submit(self):
        name = self.name_entry.get()
        gender = self.gender_combo.get()
        location = self.address_entry.get()
        civil_status = self.cs_combo.get()
        birthdate = self.datetime.entry.get()
        email = self.email_entry.get()
        cellnum = self.cp_entry.get()

        with open('test_entries.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, gender, location, civil_status, birthdate, email, cellnum])

        self.win1.destroy()
        self.home_page.deiconify()