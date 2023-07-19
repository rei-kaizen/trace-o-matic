from tkinter import *
from consent_form import DataPrivacy
import tkinter.ttk as ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import csv
class SignUpWindow():
    def __init__(self, parent):
        
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.geometry("500x600")
        self.win.title('Registration')

        # user information input fields
        heading_label = Label(self.win, text="Sign Up", font=("Arial Rounded MT Bold", 20))
        heading_label.place(x=20, y=10)

        subheading_label = Label(self.win, text="Enter your details to create your entry", font=("Cobrel", 11), fg="gray")
        subheading_label.place(x=20, y=50)
        
        # full name
        name_label = Label(self.win, text="Full Name", font=("Corbel", 10), fg="black")
        name_label.place(x=20, y=100)
        
        self.name_entry = Entry(self.win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        self.name_entry.place(x=20, y=120)
        
        #gender
        gender_label = Label(self.win, text="Gender", font=("Corbel", 10), fg="black")
        gender_label.place(x=300, y=100)
        
        self.gender_combo = ttk.Combobox(self.win, values=["Female", "Male"], font=("Corbel", 10))
        self.gender_combo.place(x=300, y=120)
        
        # address
        address_label = Label(self.win, text="Address", font=("Corbel", 10), fg="black")
        address_label.place(x=20, y=170)
        
        self.address_entry = Entry(self.win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        self.address_entry.place(x=20, y=190)
        
        #civil status
        cs_label = Label(self.win, text="Civil Status", font=("Corbel", 10), fg="black")
        cs_label.place(x=300, y=170)
        
        self.cs_combo = ttk.Combobox(self.win, values=["Annuled", "Cohabiting", "Divorce", "Not Specified", "Married", "Separated", "Single", "Widowed"], font=("Corbel", 10))
        self.cs_combo.place(x=300, y=190)
        
        # cellphone
        cellphone_label = Label(self.win, text="Cellphone", font=("Corbel", 10), fg="black")
        cellphone_label.place(x=20, y=240)
        
        self.cellphone_entry = Entry(self.win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        self.cellphone_entry.place(x=20, y=260)
        
        # birth date
        self.calendar = tb.DateEntry(self.win)
        self.calendar.place(x=300, y=240)
        
        # calendar_button = ttk.Button(self.win, text="Get Date", command=self.get_bday)
        # calendar_button.place(x=340, y=280)

        # landline
        landline_label = Label(self.win, text="Landline", font=("Corbel", 10), fg="black")
        landline_label.place(x=20, y=310)
        
        self.landline_entry = Entry(self.win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        self.landline_entry.place(x=20, y=330)
        
        # checkbutton for consent
        agree_button = Checkbutton(self.win, text="I Agree to", font=("Corbel", 10), activebackground="#39767A")
        agree_button.place(x=20, y=375)
        
        #consent
        consent_button = tb.Button(self.win, text="Data Privacy Consent.", bootstyle="light", command= self.consent)
        consent_button.place(x=100, y=375)

        # submit button
        submit_button = tb.Button(self.win, text="Submit",  bootstyle="info", command= self.submit)
        submit_button.place(x=20, y=420)
        
        # cancel button
        cancel_button = tb.Button(self.win, text="Cancel", bootstyle="info-outline", command=self.close_window)
        cancel_button.place(x=100, y=420)
    
        
        self.win.mainloop()

    def close_window(self):
        self.win.destroy()
    
    def consent(self):
        DataPrivacy(self.win)
    
    def submit(self):
        name = self.name_entry.get()
        gender = self.gender_combo.get()
        location = self.address_entry.get()
        civil_status = self.cs_combo.get()
        birthdate = self.calendar.entry.get()
        cellphone = self.cellphone_entry.get()
        landline = self.landline_entry.get()
        
        # Save the file using CVS
        with open('entries.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, gender, location, civil_status, birthdate, cellphone, landline])
        
        self.win.destroy()