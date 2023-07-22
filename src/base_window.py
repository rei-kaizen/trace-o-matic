from tkinter import *
from PIL import ImageTk, Image

class BaseWindow(Toplevel):
    def __init__(self, parent, title, image_path):
        super().__init__(parent)
        self.title(title)
        self.geometry("1000x600")

        bg = Image.open(image_path)
        bg = bg.resize((1000, 600), Image.LANCZOS)

        self.bg_image = ImageTk.PhotoImage(bg)
        self.bg_label = Label(self, image=self.bg_image)
        self.bg_label.pack()
        
class AboutWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, "About", "assets/about-p.png")

class FAQWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, "Frequently Asked Questions", "assets/faqs-p.png")