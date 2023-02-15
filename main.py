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
 
# Initialize the stopwatch variables
elapsed_time = 0
timer_running = False
 
# Define a function to update the stopwatch
def update_stopwatch():
    global elapsed_time, timer_running
    if timer_running:
        elapsed_time += 1
        canvas.itemconfig(timer_text, text="Time: {}s".format(elapsed_time))
    canvas.after(1000, update_stopwatch)
 
# Define a function to start the stopwatch
def start_stopwatch():
    global timer_running
    timer_running = True
 
# Define a function to stop the stopwatch
def stop_stopwatch():
    global timer_running
    timer_running = False



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

timer_text = canvas.create_text(50, 50, text="Time: 0s", fill="black", font=("Arial", 16, "bold"))

canvas.pack()
# Create a label widget and add it to the window
label = tk.Label(window, text="Binge Snake!")
label.pack()
 
# Start the stopwatch
start_stopwatch()
update_stopwatch()
# Run the window
window.update()

window.mainloop()

