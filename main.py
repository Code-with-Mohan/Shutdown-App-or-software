from tkinter import*
import tkinter as tk
import os

def restarttime():
    os.system("shutdown /r /t 30")

def restart():
    os.system("shutdown /r /t 1")
    
def shutdown():
    os.system("shutdown /s /t 1")  # Use /s for shutdown
    
def logout():
    os.system("shutdown /l")  # Use /l for logout
    
# Create the main window
root = tk.Tk()
root.title("Shutdown App")
root.geometry("400x580")  # Set the size of the window
# Set the window icon
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)


# First button
restart_time_button = PhotoImage(file="restart time.png")
first_button = Button(root, image=restart_time_button, borderwidth=0, cursor="hand2", command=restarttime)
first_button.place(x=10, y=10)

# Second button
close_button = PhotoImage(file="close.png")
second_button = Button(root, image=close_button, borderwidth=0, cursor="hand2", command=root.destroy)
second_button.place(x=200, y=10)

# Third button
restart_button = PhotoImage(file="restart.png")
third_button = Button(root, image=restart_button, borderwidth=0, cursor="hand2", command=restart)
third_button.place(x=10, y=200)

# Fourth button
shutdown_button = PhotoImage(file="shutdown.png")
fourth_button = Button(root, image=shutdown_button, borderwidth=0, cursor="hand2", command=shutdown)
fourth_button.place(x=200, y=200)

# Fifth button
logout_button = PhotoImage(file="log out.png")
fifth_button = Button(root, image=logout_button, borderwidth=0, cursor="hand2", command=logout)
fifth_button.place(x=10, y=400)

# Run the Tkinter event loop
root.mainloop()
