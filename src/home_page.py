import imageio
import tkinter as tk
from tkinter import Frame, Label, Canvas, NW
from PIL import Image, ImageTk
from ttkbootstrap import Style, Button
from signup_page import SignUpWindow
from search_box import SearchWindow
from base_window import AboutWindow, FAQWindow

class HomeWindow(tk.Tk):
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 500
    GIF_FRAME_DELAY = 100 

    def __init__(self):
        super().__init__()

        self.window_properties()
        self.icons()
        self.banner()
        self.set_animated_gif()
        self.set_buttons()

    def window_properties(self):
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.title('Trace-O-Matic')
        self.ttk_style = Style(theme='litera')

    def icons(self):
        logo = Image.open("assets/tom-logo.png").resize((50, 50), Image.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo)
        self.iconphoto(False, self.logo_img)

        newntry_icon = Image.open("assets/add-icon1.jpg").resize((20, 20), Image.LANCZOS)
        self.newntry_icon_img = ImageTk.PhotoImage(newntry_icon)

    def banner(self):
        head_frame = Frame(self, width=self.WINDOW_WIDTH, height=120, bg="white")
        head_frame.pack()

        logo_label = Label(head_frame, image=self.logo_img, bg="white")
        logo_label.place(x=490, y=0)

        title_label = Label(head_frame, text="Trace-O-Matic", font=("Gadugi 10 bold"), fg="black", bg="white")
        title_label.place(x=470, y=50)

        newntry_icon_label = Label(head_frame, image=self.newntry_icon_img, bg="white")
        newntry_icon_label.place(x=770, y=90)
    
    def set_buttons(self):
        self.signup_button = self.create_button("Sign Up", 480, 440, "success", self.sign_up)
        self.search_button = self.create_button("\U0001F50D  Search....", 80, 90, "light", self.search)
        self.home_button = self.create_button("Home", 400, 90, "light", self.on_home)
        self.about_button = self.create_button("About", 500, 90, "light", self.on_about)
        self.faq_button = self.create_button("FAQ", 600, 90, "light", self.on_faq)
        self.newntry_button = self.create_button("New Entry", 820, 87, "light", self.sign_up)

    def set_animated_gif(self):
        gif_path = "assets/newbg.gif"
        self.gif_frames = self.load_gif_frames(gif_path)
        self.current_frame = 0
        self.canvas = Canvas(self, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT, highlightthickness=0)
        self.canvas.pack()
        self.animate_gif()

    def load_gif_frames(self, gif_path):
        with imageio.get_reader(gif_path) as reader:
            frames = [ImageTk.PhotoImage(Image.fromarray(frame_data).resize((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), Image.LANCZOS))
                      for frame_data in reader]
        return frames

    def animate_gif(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.gif_frames[self.current_frame], anchor=NW)
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.after(self.GIF_FRAME_DELAY, self.animate_gif)
    
    def create_button(self, text, x, y, bootstyle, command):
        button = Button(self, text=text, bootstyle=bootstyle, command=command)
        button.place(x=x, y=y)

        return button

    def sign_up(self):
        self.withdraw()
        SignUpWindow(self)

    def search(self):
        SearchWindow(self)

    def on_home(self):
        self.deiconify()

    def on_about(self):
        AboutWindow(self)

    def on_faq(self):
        FAQWindow(self)