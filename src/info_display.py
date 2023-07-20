from tkinter import *
from ttkbootstrap import *

class OutputWindow:
    def __init__(self, sideparent, user_info):
        self.sideparent = sideparent
        self.user_info = user_info
        self.top = Toplevel(sideparent)
        self.top.geometry("250x120")
        self.top.title("User Information")

        self.info_label = Label(self.top, text="", justify=LEFT)
        self.info_label.pack(pady=5)

        self.show_info()

    def show_info(self):
        user_info = self.user_info
        self.info_label.config(text=f"Name: {user_info[0]}\n"
                                f"Gender: {user_info[1]}\n"
                                f"Address: {user_info[2]}\n"
                                f"Civil Status: {user_info[3]}\n"
                                f"Birthday: {user_info[4]}\n"
                                f"Email: {user_info[5]}\n"
                                f"Phone Number: {user_info[6]}")
