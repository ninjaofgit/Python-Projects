from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def shutdown():
    os.system("shutdown /s /t 1")
   

st = Tk()   # Creating a Window
st.title("ShutDown Panel")    # Giving a Title 
st.geometry("500x500")  # Dimensions
bg = PhotoImage(file = "Aditya_logo.png")

label = Label(st , image = bg)
label.place(x=0,y=0)

r_button = Button(st, text = "Restart", font = ("ROBOTO", 20, "bold"), relief = RAISED, cursor = "arrow", command=restart, bg="red2")   # Creating Restart Button
r_button.place(x=150, y=100, height=50, width=200)    # Height & Width

rt_button = Button(st, text = "Delay", font = ("ROBOTO", 20, "bold"), relief = RAISED, cursor = "plus", command=restart_time, bg="firebrick1")   # Creating Restart Button
rt_button.place(x=150, y=225, height=50, width=200)    # Height & Width

st_button = Button(st, text = "ShutDown", font = ("ROBOTO", 20, "bold"), relief = RAISED, cursor = "plus", command = shutdown, bg="orangered2")   # Creating Restart Button
st_button.place(x=150, y=360, height=50, width=200)    # Height & Width

st.mainloop()
