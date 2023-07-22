import tkinter as tk
from tkinter import Frame, Label, Canvas
from tkinter.constants import NW
from PIL import Image, ImageTk
from ttkbootstrap import Style, Button
from signup_page import SignUpWindow
from search_box import SearchWindow
from base_window import AboutWindow, FAQWindow
import imageio

class HomeWindow(tk.Tk):
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 500
    GIF_FRAME_DELAY = 100 

    def __init__(self):
        super().__init__()

        self.set_window_properties()
        self.set_header_frame()
        self.set_animated_gif()
        self.set_buttons()

    def set_window_properties(self):
        self.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.title('Trace-O-Matic')
        self.ttk_style = Style(theme='litera')
        self.set_icon()

    def set_icon(self):
        logo = Image.open("assets/tom-logo.png").resize((50, 50), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(logo)
        self.iconphoto(False, self.logo_photo)

    def set_header_frame(self):
        header_frame = Frame(self, width=self.WINDOW_WIDTH, height=120, bg="white")
        header_frame.pack()

        # labels
        logo_label = Label(header_frame, image=self.logo_photo, bg="white")
        logo_label.place(x=490, y=0)

        title_label = Label(header_frame, text="Trace-O-Matic", font=("Gadugi 10 bold"), fg="black", bg="white")
        title_label.place(x=470, y=50)

        #icon image
        icon1 = Image.open("assets/add-icon1.jpg").resize((20, 20), Image.LANCZOS)
        self.icon1_photo = ImageTk.PhotoImage(icon1)
        icon1_label = Label(header_frame, image=self.icon1_photo, bg="white")
        icon1_label.place(x=800, y=90)

    def create_button(self, text, x, y, bootstyle, command):
        button = Button(self, text=text, bootstyle=bootstyle, command=command)
        button.place(x=x, y=y)
        return button
    
    def set_buttons(self):
        self.signup_button = self.create_button("Sign Up", 480, 440, "success", self.sign_up)
        self.search_button = self.create_button("\U0001F50D  Search....", 80, 90, "light", self.search)
        self.home_button = self.create_button("Home", 400, 90, "light", self.on_home)
        self.about_button = self.create_button("About", 500, 90, "light", self.on_about)
        self.faq_button = self.create_button("FAQ", 600, 90, "light", self.on_faq)
        self.add_button = self.create_button("New Entry", 820, 87, "light", self.sign_up)

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


if __name__ == "__main__":
    home_window = HomeWindow()
    home_window.mainloop()