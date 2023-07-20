from tkinter import *
from PIL import ImageTk, Image

class AboutWindow:
    def __init__(self, parent):
        self.home_page = parent
        self.win = Toplevel(parent)
        self.win.title("About")

        about_bg = Image.open("assets/about-p.png")
        self.about_bg_image = ImageTk.PhotoImage(about_bg)
        self.about_bg_label = Label(self.win, image=self.about_bg_image)  
        self.about_bg_label.pack() 

if __name__ == "__main__":
    root = Tk()
    about_window = AboutWindow(root)
    root.mainloop()
