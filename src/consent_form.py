from tkinter import *

class DataPrivacy:
    WINDOW_WIDTH = 900
    WINDOW_HEIGHT = 600

    def __init__(self, parent):
        self.parent = parent
        self.win2 = Toplevel(parent)

        self.window_properties()
        self.banner()
        self.consent_content()
        self.close_button()

        self.win2.mainloop()

    def window_properties(self):
        self.win2.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.win2.title('DATA PRIVACY CONSENT')

    def banner(self):
        heading = Label(self.win2, text="DATA PRIVACY CONSENT", font=("Arial Rounded MT Bold", 20))
        heading.pack(pady=10)
        line = Label(self.win2, text="-"*100, font=("Arial Rounded MT Bold", 10))
        line.pack(pady=10)

    def consent_content(self):
        text = """By clicking "I Agree," you confirm that you willingly and voluntarily give consent 
for the collection and processing of your data for the purposes outlined below.

This app may collect and process your personal information 
and/or sensitive information for the following purposes:

(a) Health update processing and tracking
(b) Emergency response purposes
(c) Tracing activities necessary for the containment of COVID-19

You understand that there is a Privacy Notice available, and you acknowledge that you have read it. 
You give your consent to collect, store, access, and/or process the personal data you provide, such as 
your name, address, phone number, and email address, for the duration specified in the app's policies. 
You recognize that the collection and processing of your personal data are necessary to achieve the aforementioned purposes.

You are aware of your rights, including the right to be informed, the right to access, the right to object, the right to 
erasure or blocking, the right to damages, the right to file a complaint, the right to rectify, and the right to data portability. 
You understand that specific procedures, conditions, and exceptions must be followed to exercise or invoke these rights.

By continuing to use this app, you agree to these terms and conditions regarding data privacy. 
If you do not agree, please refrain from using the app."""

        consent_label = Label(self.win2, text=text, font=("Corbel", 12), justify=LEFT)
        consent_label.pack(pady=10)

    def close_button(self):
        close = Button(self.win2, text="Close", font=("Corbel", 10), fg="#286A6F", bg="#B4DDDA", activebackground="#1E5256", bd=1, height=2, width=10, command=self.close_window)
        close.pack(side=BOTTOM, pady=10)

    def close_window(self):
        self.win2.destroy()
