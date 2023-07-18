
from tkinter import *
from PIL import Image, ImageTk
from consent_form import DataPrivacy

class SignUpWindow:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.geometry("1000x600")
        self.win.title('Trace-O-Matic')
        
        #logo icon
        logo = Image.open("assets/tom-logo.png")
        logo = ImageTk.PhotoImage(logo)
        self.win.iconphoto(False, logo)

        # user information input fields
        heading_label = Label(self.win, text="Sign Up", font=("Arial Rounded MT Bold", 20))
        heading_label.place(x=20, y=10)

        subheading_label = Label(self.win, text="Enter your details to create your entry", font=("Cobrel", 11), fg="gray")
        subheading_label.place(x=20, y=50)
        
        # full name
        name_label = Label(self.win, text="Full Name", font=("Corbel", 10), fg="black")
        name_label.place(x=20, y=100)
        
        name_entry = Entry(self.win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        name_entry.place(x=20, y=120)
        
        # address
        address_label = Label(self.win, text="Address", font=("Corbel", 10), fg="black")
        address_label.place(x=20, y=150)
        
        address_entry = Entry(self.win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        address_entry.place(x=20, y=180)
        
        # cellphone
        cellphone_label = Label(self.win, text="Cellphone", font=("Corbel", 10), fg="black")
        cellphone_label.place(x=20, y=210)
        
        cellphone_entry = Entry(self.win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        cellphone_entry.place(x=20, y=240)
        
        # landline
        landline_label = Label(self.win, text="Landline", font=("Corbel", 10), fg="black")
        landline_label.place(x=20, y=270)
        
        landline_entry = Entry(self.win, font=("Corbel", 9), fg="black", width=40, bd=1, bg="#E8E6E5")
        landline_entry.place(x=20, y=300)
        
        
        # checkbutton for consent
        agree_radio = Checkbutton(self.win, text="I Agree to", font=("Corbel", 8), activebackground="#39767A")
        agree_radio.place(x=20, y=375)
        
        #consent
        consent_button = Button(self.win, text="Data Privacy Consent.", font=("Corbel", 9), fg="#39767A", activeforeground="blue", bd=0, command= self.consent)
        consent_button.place(x=100, y=375)

        # submit button
        submit_button = Button(self.win, text="Submit", font=("Corbel", 10), fg="white", bg="#286A6F", bd=1, height=2, width=10, activebackground="#1E5256", command= self.submit)
        submit_button.place(x=20, y=400)
        
        # cancel button
        cancel_button = Button(self.win, text="Cancel", font=("Corbel", 10), fg="#286A6F", bg="#B4DDDA", activebackground="#1E5256", bd=1, height=2, width=10, command=self.close_window)
        cancel_button.place(x=120, y=400)
        
        self.win.mainloop()

    def close_window(self):
        self.win.destroy()
    
    def submit(self):
        self.win.destroy()
    
    def consent(self):
        DataPrivacy(self.win)
        
