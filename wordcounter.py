##################################################
## Word Counter
## Simple utility to read whatever is in the clipboard buffer, 
## count the words (space-separated text), and display that number.
##################################################
## None at the moment.
##################################################
## Author: Leon Adato
## Copyright: Copyright 2023
## Credits: Rachel Foster, Tom Schimansky (of customtkinter fame), and my wife Debbie
## License: none
## Version: 0.0.1
## Mmaintainer: Leon Adato
## Email: wordcounter@adatosystems.com
## Status: alpha
##################################################
## NOTES:
## make sure you've installed both 
##   tkinter (typically with apt install python3-tk)
##   and customtkinter (typically with pip3 install customtkinter)

import customtkinter

class MyInstructionsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = customtkinter.CTkLabel(self, wraplength=150, text="Copy your text into the clipboard, then click the button below to get the count of words.")
        self.label_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")

class MyWordCountFrame(customtkinter.CTkFrame):
    def __init__(self, master, wrdcnt):
        super().__init__(master)
        self.wrdcnt = "nope"
        
        self.label_2 = customtkinter.CTkLabel(self, text=wrdcnt, fg_color="transparent", font=('Arial', 32))
        self.label_2.place(relx=0.5, rely=0.5, anchor="center")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Word Counter")
        self.geometry("400x200")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame_1 = MyInstructionsFrame(self)
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.checkbox_frame_2 = MyWordCountFrame(self, wrdcnt="0")
        self.checkbox_frame_2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.checkbox_frame_2.configure(fg_color="transparent")

        self.button_1 = customtkinter.CTkButton(self, text="Count Words Now", command=self.wordcount)
        self.button_1.grid(row=3, column=0, padx=10, pady=(10, 2), sticky="ew", columnspan=2)

        self.button_2 = customtkinter.CTkButton(self, text="Exit", command=self.destroy)
        self.button_2.grid(row=4, column=0, padx=10, pady=(2, 10), sticky="ew", columnspan=2)

    def wordcount(self):
        """Pull contents of clipboard and count words
        """
        numwords = len(self.selection_get(selection="CLIPBOARD").split())
        self.checkbox_frame_2.label_2.configure(text=f"{str(numwords)}")

app = App()
app.mainloop()