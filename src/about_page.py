from tkinter import *
from PIL import ImageTk, Image

class AboutWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")
        self.geometry("1000x600")

        # Load the image and resize it
        about_bg = Image.open("assets/about-p.png")
        about_bg = about_bg.resize((1000, 600), Image.LANCZOS)

        # Display the image
        self.about_bg_image = ImageTk.PhotoImage(about_bg)
        self.about_bg_label = Label(self, image=self.about_bg_image)
        self.about_bg_label.pack()