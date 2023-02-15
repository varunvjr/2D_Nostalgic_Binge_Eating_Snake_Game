import tkinter as tk
import random
# 2d Snake Game Board Dimensions

WIDTH = 1000
HEIGHT = 700
BACKGROUND = "#5af5aa"
FOOD = 10


#Trying to add food comp
x = random.randint(0, WIDTH - FOOD)
y = random.randint(0, HEIGHT - FOOD)

# Create a new window
window = tk.Tk()

# Set the title of the window
window.title("Welcome to 2D snake game")

# Set the size of the window
canvas = tk.Canvas(window, bg=BACKGROUND,
                height=HEIGHT, width=WIDTH)
canvas.create_oval(x, y, x+FOOD, y+FOOD, fill="black")
canvas.pack()
# Create a label widget and add it to the window
label = tk.Label(window, text="Binge Snake!")
label.pack()

# Run the window
window.update()
window.mainloop()
