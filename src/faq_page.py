from tkinter import *
from PIL import ImageTk, Image
class FAQWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Frequently Asked Questions")
        self.geometry("1000x600")

        # Load the image and resize it
        faqs_bg = Image.open("assets/faqs-p.png")
        faqs_bg = faqs_bg.resize((1000, 600), Image.LANCZOS)

        # Display the image
        self.faqs_bgi = ImageTk.PhotoImage(faqs_bg)
        self.about_bg_label = Label(self, image=self.faqs_bgi)
        self.about_bg_label.pack()
