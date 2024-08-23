import tkinter as tk
from tkinter import messagebox

def show_popup():
    # Creating the Main Window
    root = tk.Tk()
    root.withdraw() # hide the window

    root.attributes("-topmost", True)   # to set the main window on the top
    
    messagebox.showinfo("Verified \u2611")

    root.destroy()  # Destroy the main window after the message box is closed

email = input("Enter your Email: ")
k,j,d = 0, 0, 0
# shortest email: g@g.in
if(len(email) >= 6):    # Length Condition
    if email[0].isalpha():  # First character = alphabet
        if ('@' in email) and (email.count('@') == 1):  # Condition for '@'
            if (email[-4] == '.') ^ (email[-3] == '.') ^ (email[-3] == '.' and email[-6] == '.'):   # Condition for '.'
                for i in email:
                    if i.isspace():    # Condition for Space " "
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():  # Uppercase Condition
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")   
                show_popup()     
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")
