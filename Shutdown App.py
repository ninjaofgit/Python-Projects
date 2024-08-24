from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()   # Creating a Window
st.title("ShutDown App")    # Giving a Title 
st.geometry("500x500")  # Dimensions
st.config(bg="medium spring green")

r_button = Button(st, text = "Restart", font = ("ROBOTO", 20, "bold"), relief = RAISED, cursor = "plus", command=restart())   # Creating Restart Button
r_button.place(x=150, y=60, height=50, width=200)    # Height & Width

rt_button = Button(st, text = "Restart Time", font = ("ROBOTO", 20, "bold"), relief = RAISED, cursor = "plus", command=restart_time())   # Creating Restart Button
rt_button.place(x=150, y=170, height=50, width=200)    # Height & Width

lg_button = Button(st, text = "Log-Out", font = ("ROBOTO", 20, "bold"), relief = RAISED, cursor = "plus", command = logout())   # Creating Restart Button
lg_button.place(x=150, y=270, height=50, width=200)    # Height & Width

st_button = Button(st, text = "ShutDown", font = ("ROBOTO", 20, "bold"), relief = RAISED, cursor = "plus", command = shutdown())   # Creating Restart Button
st_button.place(x=150, y=370, height=50, width=200)    # Height & Width

st.mainloop()
