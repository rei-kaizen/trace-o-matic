from tkinter import *
from PIL import Image, ImageTk
import imageio
from signup_page import SignUpWindow
from test_search_page import SearchWindow

class HomeWindow:
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
        search = Label(header_frame, text="\U0001F50D", font=("Corbel", 11), bg="white")
        search.place(x=60, y=85)
        
        # search button
        self.search_button = Button(text="Search....", font=("Corbel", 9),  bd=0, bg="white", activebackground="#D9EAE9", command=self.search)
        self.search_button.place(x=80, y=90)
        
        # home button
        self.home_button = Button(header_frame, text="Home", font=("Corbel", 9),  bd=0, bg="white", activebackground="#D9EAE9", command=self.on_home)
        self.home_button.place(x=400, y=90)

        # About button
        self.about_button = Button(header_frame, text="About", font=("Corbel", 9), bd=0, bg="white", activebackground="#D9EAE9", command=self.on_about)
        self.about_button.place(x=500, y=90)
        
        # FAQ button
        self.faq_button = Button(header_frame, text="FAQ", font=("Corbel",9), bd=0, bg="white", activebackground="#D9EAE9", command=self.on_faq)
        self.faq_button.place(x=600, y=90)

        # add an entry icon
        icon1 = Image.open("assets/add-icon1.jpg")
        icon1 = icon1.resize((20, 20), Image.LANCZOS)
        icon1 = ImageTk.PhotoImage(icon1)
        icon1_label = Label(header_frame, image=icon1, bg="white")
        icon1_label.place(x=800, y=90)
        
        # add button
        self.add_button = Button(header_frame, text="New Entry", font=("Corbel",9), bd=0, bg="white", activeforeground="#286A6F", command=self.sign_up)
        self.add_button.place(x=820, y=90)
        
        # entry counter
        icon2 = Image.open("assets/entries-icon2.png")
        icon2 = icon2.resize((20, 20), Image.LANCZOS)
        icon2 = ImageTk.PhotoImage(icon2)
        icon2_label = Label(header_frame, image=icon2, bg="white")
        icon2_label.place(x=900, y=90)
    
        # load the animated GIF
        gif_path = "assets/home-bg4.gif"
        self.gif_frames = self.load_gif_frames(gif_path)
        self.current_frame = 0

        # canvas to display the animated GIF
        self.canvas = Canvas(self.win, width=1000, height=600, highlightthickness=0)
        self.canvas.pack()
        self.animate_gif()

        # slogan for welcome page
        slogan_label = Label(self.win, text=" SMART TRACE, ", font=("Arial Rounded MT Bold", 25), fg="white", bg="green")
        slogan_label.place(x=380, y=250)
        slogan_label1 = Label(self.win, text=" SAFEGUARDING EVERY PLACE ", font=("Arial Rounded MT Bold", 25), fg="white", bg="green")
        slogan_label1.place(x=250, y=300)
        
        # sign up button
        signup_button = Button(self.win, text="Sign Up", font=("Corbel", 10), height=2, width=10, bd=1, bg="#CFCF5A", activebackground="#8DAEA0", command=self.sign_up)
        signup_button.place(x=475, y=370)
        
        #run window
        self.win.mainloop()
        
    def sign_up(self):
        SignUpWindow(self.win)
    
    def search(self):
        SearchWindow(self.win)
        
    def load_gif_frames(self, gif_path):
        gif = imageio.mimread(gif_path)
        frames = []
        for frame_data in gif:
            frame = Image.fromarray(frame_data)
            frame = frame.resize((1000, 600), Image.LANCZOS)  # Resize the frame
            frames.append(ImageTk.PhotoImage(frame))
        return frames

    def animate_gif(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.gif_frames[self.current_frame], anchor="nw")  # Adjust the y coordinate
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.win.after(100, self.animate_gif)
        
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

HomeWindow()