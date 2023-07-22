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
        self.set_signup_button()

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

        # buttons
        self.search_button = Button(header_frame, text="\U0001F50D  Search....", bootstyle="light", command=self.search)
        self.search_button.place(x=80, y=90)

        self.home_button = Button(header_frame, text="Home", bootstyle="light", command=self.on_home)
        self.home_button.place(x=400, y=90)

        self.about_button = Button(header_frame, text="About", bootstyle="light", command=self.on_about)
        self.about_button.place(x=500, y=90)

        self.faq_button = Button(header_frame, text="FAQ", bootstyle="light", command=self.on_faq)
        self.faq_button.place(x=600, y=90)

        self.add_button = Button(header_frame, text="New Entry", bootstyle="light", command=self.sign_up)
        self.add_button.place(x=820, y=87)

        #icon image
        icon1 = Image.open("assets/add-icon1.jpg").resize((20, 20), Image.LANCZOS)
        self.icon1_photo = ImageTk.PhotoImage(icon1)
        icon1_label = Label(header_frame, image=self.icon1_photo, bg="white")
        icon1_label.place(x=800, y=90)

    def set_animated_gif(self):
        gif_path = "assets/newbg.gif"
        self.gif_frames = self.load_gif_frames(gif_path)
        self.current_frame = 0
        self.canvas = Canvas(self, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT, highlightthickness=0)
        self.canvas.pack()
        self.animate_gif()

    def set_signup_button(self):
        signup_button = Button(self, text="Sign Up", bootstyle="success", command=self.sign_up)
        signup_button.place(x=480, y=440)

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