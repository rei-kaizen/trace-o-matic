from tkinter import *
import tkinter.ttk as ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from consent_form import DataPrivacy
import csv

class SignUpWindow:
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 600
    GENDER_VALUES = ["Female", "Male"]
    CS_VALUES = ["Annuled", "Cohabiting", "Divorce", "Not Specified", "Married", "Separated", "Single", "Widowed"]

    def __init__(self, home_page):
        self.home_page = home_page
        self.su_win = Toplevel(home_page)

        self.set_window_properties()
        self.create_user_input_fields()
        self.create_checkbuttons()
        self.create_submit_and_cancel_buttons()

        self.su_win.mainloop()

    def set_window_properties(self):
        self.su_win.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.su_win.title('Registration')

        heading_label = Label(self.su_win, text="Sign Up", font=("Arial Rounded MT Bold", 20))
        heading_label.place(x=20, y=10)

        subheading_label = Label(self.su_win, text="Enter your details to create your entry", font=("Cobrel", 11), fg="gray")
        subheading_label.place(x=20, y=50)

    def create_user_input_fields(self):
        self.name_entry = self.create_input_field("Full Name", 20, 100, 40)
        self.gender_combo = self.create_combobox("Gender", self.GENDER_VALUES, 300, 100)
        self.address_entry = self.create_input_field("Address", 20, 170, 40)
        self.cs_combo = self.create_combobox("Civil Status", self.CS_VALUES, 300, 170)
        self.emeil_entry = self.create_input_field("Email", 20, 240, 40)
        self.calendar = self.create_calendar(300, 240)
        self.cp_entry = self.create_input_field("Phone Number", 20, 310, 40)

    def create_input_field(self, label_text, x_pos, y_pos, width):
        label = Label(self.su_win, text=label_text, font=("Corbel", 10), fg="black")
        label.place(x=x_pos, y=y_pos)

        entry = Entry(self.su_win, font=("Corbel", 9), fg="black", width=width, bd=1, bg="#E8E6E5")
        entry.place(x=x_pos, y=y_pos+20)

        return entry

    def create_combobox(self, label_text, values, x_pos, y_pos):
        label = Label(self.su_win, text=label_text, font=("Corbel", 10), fg="black")
        label.place(x=x_pos, y=y_pos)

        combo = ttk.Combobox(self.su_win, values=values, font=("Corbel", 10))
        combo.place(x=x_pos, y=y_pos+20)

        return combo

    def create_calendar(self, x_pos, y_pos):
        calendar = tb.DateEntry(self.su_win)
        calendar.place(x=x_pos, y=y_pos)

        return calendar

    def create_checkbuttons(self):
        agree_button = Checkbutton(self.su_win, text="I Agree to", font=("Corbel", 10), activebackground="#39767A")
        agree_button.place(x=20, y=375)

        consent_button = tb.Button(self.su_win, text="Data Privacy Consent.", bootstyle="light", command=self.consent)
        consent_button.place(x=100, y=375)

    def create_submit_and_cancel_buttons(self):
        submit_button = tb.Button(self.su_win, text="Submit",  bootstyle="info", command=self.submit)
        submit_button.place(x=20, y=420)

        cancel_button = tb.Button(self.su_win, text="Cancel", bootstyle="info-outline", command=self.close_window)
        cancel_button.place(x=100, y=420)

    def close_window(self):
        self.su_win.destroy()
        self.home_page.deiconify()

    def consent(self):
        DataPrivacy(self.su_win)

    def submit(self):
        name = self.name_entry.get()
        gender = self.gender_combo.get()
        location = self.address_entry.get()
        civil_status = self.cs_combo.get()
        birthdate = self.calendar.entry.get()
        email = self.emeil_entry.get()
        cellnum = self.cp_entry.get()

        with open('test_entries.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, gender, location, civil_status, birthdate, email, cellnum])

        self.su_win.destroy()
        self.home_page.deiconify()