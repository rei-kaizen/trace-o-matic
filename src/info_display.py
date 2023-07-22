from tkinter import *
from ttkbootstrap import *

class OutputWindow:
    WINDOW_WIDTH = 250
    WINDOW_HEIGHT = 120

    def __init__(self, side_parent, user_info):
        self.side_parent = side_parent
        self.user_info = user_info
        self.top = Toplevel(side_parent)
        
        self.window_properties()
        self.create_info_label()
        self.show_info()

    def window_properties(self):
        self.top.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.top.title("User Information")

    def create_info_label(self):
        self.info_label = Label(self.top, text="", justify=LEFT)
        self.info_label.pack(pady=5)

    def show_info(self):
        name, gender, address, civil_status, birthday, email, phone_number = self.user_info
        self.info_label.config(text=f"Name: {name}\n"
                                f"Gender: {gender}\n"
                                f"Address: {address}\n"
                                f"Civil Status: {civil_status}\n"
                                f"Birthday: {birthday}\n"
                                f"Email: {email}\n"
                                f"Phone Number: {phone_number}")