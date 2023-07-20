from tkinter import *
from PIL import ImageTk, Image

class FAQWindow:
    def __init__(self, parent):
        self.home_page = parent
        self.win = Toplevel(parent)
        self.win.title("Frequently Asked Questions")

        faqs_bg = Image.open("assets/faqs-p.png")
        self.faqs_bg_image = ImageTk.PhotoImage(faqs_bg)  
        self.faqs_bg_label = Label(self.win, image=self.faqs_bg_image)  
        self.faqs_bg_label.pack()

if __name__ == "__main__":
    root = Tk()
    faq_window = FAQWindow(root)
    root.mainloop()
