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
        title_label = Label(header_frame, text="Trace-O-Matic", font=("Oswald 10 bold"), fg="black", bg="white")
        title_label.place(x=470, y=50)

        # search engine
        search = Label(header_frame, text="\U0001F50D", font=("Muli", 13), bg="white")
        search.place(x=50, y=90)

        # search entry
        self.search_entry = Entry(header_frame, borderwidth=0, bg="white")
        self.search_entry.place(x=80, y=97)

        self.search_entry.insert(0, "Search...")
        self.search_entry.bind("<FocusIn>", self.clear_search_text)
        self.search_entry.config(fg="gray")

        # home button
        self.home_button = Button(header_frame, text="Home", font=("Muli", 9),  borderwidth=0, bg="white", command=self.on_home)
        self.home_button.place(x=400, y=90)

        # About button
        self.faq_button = Button(header_frame, text="About", font=("Muli", 9), borderwidth=0, bg="white", command=self.on_about)
        self.faq_button.place(x=500, y=90)
        
        # FAQ button
        self.faq_button = Button(header_frame, text="FAQ", font=("Muli",9), borderwidth=0, bg="white", command=self.on_faq)
        self.faq_button.place(x=600, y=90)


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
