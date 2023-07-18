from tkinter import *

class Interface:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("1000x600")
        self.win.title('Trace-O-Matic')

        # Add logo
        logo = PhotoImage(file="assets/tom-logo.png")
        self.win.iconphoto(False, logo)

        # Set the frame for the header
        header_frame = Frame(self.win, width=1000, height=100, bg="white")
        header_frame.place(x=0, y=0)

        title_label = Label(self.win, text="TRACE-O-MATIC", font=("Oswald", 10), fg="black", bg="white")
        title_label.pack(pady=20)

        # Search engine
        search = Label(header_frame, text="\U0001F50D", font=("Muli", 13), bg="white")
        search.place(x=50, y=60)

        # search entry
        self.search_entry = Entry(header_frame, borderwidth=0, bg="white")
        self.search_entry.place(x=80, y=67)

        self.search_entry.insert(0, "Search...")
        self.search_entry.bind("<FocusIn>", self.clear_search_text)
        self.search_entry.config(fg="gray")

        # home button
        self.home_button = Button(header_frame, text="Home", font=("Muli", 9),  borderwidth=0, bg="white", command=self.on_home)
        self.home_button.place(x=400, y=60)

        # About button
        self.faq_button = Button(header_frame, text="About", font=("Muli", 9), borderwidth=0, bg="white", command=self.on_about)
        self.faq_button.place(x=500, y=60)
        
        # FAQ button
        self.faq_button = Button(header_frame, text="FAQ", font=("Muli",9), borderwidth=0, bg="white", command=self.on_faq)
        self.faq_button.place(x=600, y=60)


        # slogan for welcome page
        slogan_label = Label(self.win, text="SMART TRACE,", font=("Noto Sans", 25), fg="black")
        slogan_label.place(x=400, y=200)
        slogan_label1 = Label(self.win, text="SAFEGUARDING EVERY PLACE", font=("Noto Sans", 25), fg="black")
        slogan_label1.place(x=280, y=250)
        
        # sign up button
        signup_button = Button(self.win, text="Sign Up", font=("Muli", 10), height=2, width=10, borderwidth=1, bg="white", command=self.sign_up)
        signup_button.place(x=480, y=320)

        self.win.mainloop()

    def clear_search_text(self, event):
        self.search_entry.delete(0, END)

    def on_home(self):
        # an action to go back to main page
        print("Just landed on the home screen.")
        
    def on_about(self):
        # direct to faq page
        print("Just landed on the faq")
        
    def on_faq(self):
        # direct to faq page
        print("Just landed on the faq")
    
    def sign_up(self):
        # direct to faq page
        print("Just landed on the trace form")


Interface()
