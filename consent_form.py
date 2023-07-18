from tkinter import *

class DataPrivacy:
    def __init__(self, parent):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.geometry("900x550")
        self.win.title('DATA PRIVACY CONSENT')

        # user information input fields
        heading_label = Label(self.win, text="DATA PRIVACY CONSENT", font=("Arial Rounded MT Bold", 20))
        heading_label.place(x=20, y=10)
        
        line = Label(self.win, text="-"*100, font=("Arial Rounded MT Bold", 10))
        line.place(x=20, y=50)


        # data privacy consent paragraph
        consent_text = """By clicking "I Agree," you confirm that you willingly and voluntarily give consent 
for the collection and processing of your data for the purposes outlined below.

This app may collect and process your personal information 
and/or sensitive information for the following purposes:

(a) Health update processing and tracking
(b) Emergency response purposes
(c) Tracing activities necessary for the containment of COVID-19

You understand that there is a Privacy Notice available, and you acknowledge that you have read it. 
You give your consent to collect, store, access, and/or process the personal data you provide, such as 
your name, address, telephone number, and email address, for the duration specified in the app's policies. 
You recognize that the collection and processing of your personal data are necessary to achieve the aforementioned purposes.

You are aware of your rights, including the right to be informed, the right to access, the right to object, the right to 
erasure or blocking, the right to damages, the right to file a complaint, the right to rectify, and the right to data portability. 
You understand that specific procedures, conditions, and exceptions must be followed to exercise or invoke these rights.

By continuing to use this app, you agree to these terms and conditions regarding data privacy. 
If you do not agree, please refrain from using the app."""

        consent_label = Label(self.win, text=consent_text, font=("Corbel", 12), justify=LEFT)
        consent_label.place(x=20, y=80)

        # cancel button
        close_button = Button(self.win, text="Close", font=("Corbel", 10), fg="#286A6F", bg="#B4DDDA", activebackground="#1E5256", bd=1, height=2, width=10, command=self.close_window)
        close_button.place(x=800, y=500)

        self.win.mainloop()

    def close_window(self):
        self.win.destroy()
