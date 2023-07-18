from tkinter import *
from PIL import Image, ImageTk

class Interface:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("1000x600")
        self.win.title('Trace-O-Matic')
        
        # add icon to window
        logo = Image.open("assets/tom-logo.png")
        logo = logo.resize((50, 50), Image.LANCZOS)
        logo = ImageTk.PhotoImage(logo)
        self.win.iconphoto(False, logo)

        # set the frame for the header
        header_frame = Frame(self.win, width=1000, height=120, bg="white")
        header_frame.pack()

        # display the logo image to header
        logo_label = Label(header_frame, image=logo, bg="white")
        logo_label.place(x=490, y=0)

        # title
        title_label = Label(header_frame, text="Trace-O-Matic", font=("Gadugi 10 bold"), fg="black", bg="white")
        title_label.place(x=470, y=50)

        # search engine
        search = Label(header_frame, text="\U0001F50D", font=(13), bg="white")
        search.place(x=50, y=90)

        # search entry
        self.search_entry = Entry(header_frame, borderwidth=0, bg="white")
        self.search_entry.place(x=80, y=97)

        self.search_entry.insert(0, "Search...")
        self.search_entry.bind("<FocusIn>", self.clear_search_text)
        self.search_entry.config(fg="gray")

        # home button
        self.home_button = Button(header_frame, text="Home", font=("Corbel", 9),  borderwidth=0, bg="white", command=self.on_home)
        self.home_button.place(x=400, y=90)

        # About button
        self.faq_button = Button(header_frame, text="About", font=("Corbel", 9), borderwidth=0, bg="white", command=self.on_about)
        self.faq_button.place(x=500, y=90)
        
        # FAQ button
        self.faq_button = Button(header_frame, text="FAQ", font=("Corbel",9), borderwidth=0, bg="white", command=self.on_faq)
        self.faq_button.place(x=600, y=90)

        # add an entry icon
        icon1 = Image.open("assets/add-icon1.jpg")
        icon1 = icon1.resize((20, 20), Image.LANCZOS)
        icon1 = ImageTk.PhotoImage(icon1)
        icon1_label = Label(header_frame, image=icon1, bg="white")
        icon1_label.place(x=800, y=90)
        
        # add button
        self.add_button = Button(header_frame, text="New Entry", font=("Corbel",9), borderwidth=0, bg="white", command=self.sign_up)
        self.add_button.place(x=820, y=90)
        
        # entry counter
        icon2 = Image.open("assets/entries-icon2.png")
        icon2 = icon2.resize((20, 20), Image.LANCZOS)
        icon2 = ImageTk.PhotoImage(icon2)
        icon2_label = Label(header_frame, image=icon2, bg="white")
        icon2_label.place(x=900, y=90)

        # slogan for welcome page
        slogan_label = Label(self.win, text="SMART TRACE,", font=("Corbel", 25), fg="black")
        slogan_label.place(x=400, y=250)
        slogan_label1 = Label(self.win, text="SAFEGUARDING EVERY PLACE", font=("Corbel", 25), fg="black")
        slogan_label1.place(x=280, y=300)
        
        # sign up button
        signup_button = Button(self.win, text="Sign Up", font=("Corbel", 10), height=2, width=10, borderwidth=1, bg="white", command=self.sign_up)
        signup_button.place(x=480, y=370)

        self.win.mainloop()

    def clear_search_text(self, event):
        self.search_entry.delete(0, END)

    def on_home(self):
        # an action to go back to main page
        print("Just landed on the home screen.")
        
    def on_about(self):
        # direct to faq page
        print("Just landed on the about page")
        
    def on_faq(self):
        # direct to faq page
        print("Just landed on the faq")
    
    def sign_up(self):
        # direct to faq page
        print("Just landed on the trace form")
    


Interface()
