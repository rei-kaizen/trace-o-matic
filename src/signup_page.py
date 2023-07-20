from tkinter import *
import tkinter.ttk as ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from consent_form import DataPrivacy
import csv

class SignUpWindow:
    def __init__(self, home_page):
        self.home_page = home_page
        self.su_win = Toplevel(home_page)
        self.su_win.geometry("500x600")
        self.su_win.title('Registration')

        # user information input fields
        heading_label = Label(self.su_win, text="Sign Up", font=("Arial Rounded MT Bold", 20))
        heading_label.place(x=20, y=10)

        subheading_label = Label(self.su_win, text="Enter your details to create your entry", font=("Cobrel", 11), fg="gray")
        subheading_label.place(x=20, y=50)
        
        # full name
        name_label = Label(self.su_win, text="Full Name", font=("Corbel", 10), fg="black")
        name_label.place(x=20, y=100)
        
        self.name_entry = Entry(self.su_win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        self.name_entry.place(x=20, y=120)
        
        #gender
        gender_label = Label(self.su_win, text="Gender", font=("Corbel", 10), fg="black")
        gender_label.place(x=300, y=100)
        
        self.gender_combo = ttk.Combobox(self.su_win, values=["Female", "Male"], font=("Corbel", 10))
        self.gender_combo.place(x=300, y=120)
        
        # address
        address_label = Label(self.su_win, text="Address", font=("Corbel", 10), fg="black")
        address_label.place(x=20, y=170)
        
        self.address_entry = Entry(self.su_win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        self.address_entry.place(x=20, y=190)
        
        #civil status
        cs_label = Label(self.su_win, text="Civil Status", font=("Corbel", 10), fg="black")
        cs_label.place(x=300, y=170)
        
        self.cs_combo = ttk.Combobox(self.su_win, values=["Annuled", "Cohabiting", "Divorce", "Not Specified", "Married", "Separated", "Single", "Widowed"], font=("Corbel", 10))
        self.cs_combo.place(x=300, y=190)
        
        # email
        email_label = Label(self.su_win, text="Email", font=("Corbel", 10), fg="black")
        email_label.place(x=20, y=240)
        
        self.emeil_entry = Entry(self.su_win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        self.emeil_entry.place(x=20, y=260)
        
        # birth date
        self.calendar = tb.DateEntry(self.su_win)
        self.calendar.place(x=300, y=240)

        # phone number
        cp_label = Label(self.su_win, text="Phone Number", font=("Corbel", 10), fg="black")
        cp_label.place(x=20, y=310)
        
        self.cp_entry = Entry(self.su_win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        self.cp_entry.place(x=20, y=330)
        
        # checkbutton for consent
        agree_button = Checkbutton(self.su_win, text="I Agree to", font=("Corbel", 10), activebackground="#39767A")
        agree_button.place(x=20, y=375)
        
        #consent
        consent_button = tb.Button(self.su_win, text="Data Privacy Consent.", bootstyle="light", command= self.consent)
        consent_button.place(x=100, y=375)

        # submit button
        submit_button = tb.Button(self.su_win, text="Submit",  bootstyle="info", command= self.submit)
        submit_button.place(x=20, y=420)
        
        # cancel button
        cancel_button = tb.Button(self.su_win, text="Cancel", bootstyle="info-outline", command=self.close_window)
        cancel_button.place(x=100, y=420)
    
        
        self.su_win.mainloop()

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
        
        with open('entries.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, gender, location, civil_status, birthdate, email, cellnum])
        
        self.su_win.destroy()
        self.home_page.deiconify()

if __name__ == "__main__":
    root = Tk() 
    SignUpWindow(root)
    root.mainloop()