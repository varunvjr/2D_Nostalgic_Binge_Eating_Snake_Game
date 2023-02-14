from tkinter import tk

# Create a new window
window = tk.Tk()

# Set the title of the window
window.title("Welcome to 2D snake game")

# Set the size of the window
window.geometry("300x200")

# Create a label widget and add it to the window
label = tk.Label(window, text="Hello, Player!")
label.pack()

# Run the window
window.mainloop()
