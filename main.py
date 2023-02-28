import tkinter as tk
import random
import pygame
# 2d Snake Game Board Dimensions
WIDTH = 1000
HEIGHT = 700
BACKGROUND = "#5af5aa"
FOOD = 10
BODY_SIZE = 200
SPACE_SIZE = 20
SNAKE = "#000000"
 
# Create Snake

class Snake:
        def __init__(self):
            pygame.init()
         
            self.body_size = BODY_SIZE
            self.coordinates = []
            self.squares = []
            for i in range(0, BODY_SIZE):
                self.coordinates.append([30, 30])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(
                    x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                        fill=SNAKE, tag="snake")
                self.squares.append(square)

def SnakeDisplay(snake):
        x, y = snake.coordinates[100]
        snake.coordinates.insert(0, (x, y))
        square = canvas.create_rectangle(
            x, y, x + SPACE_SIZE,
                    y + SPACE_SIZE, fill=SNAKE)
        snake.squares.insert(0, square)
 

 
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





# Create a new window
window = tk.Tk()
 
# Set the title of the window
window.title("Welcome to 2D snake game")
 
# Set the size of the window
canvas = tk.Canvas(window, bg=BACKGROUND,
                height=HEIGHT, width=WIDTH)

timer_text = canvas.create_text(50, 10, text="Time: 0s", fill="black", font=("Arial", 16, "bold"))

canvas.pack()
# Create a label widget and add it to the window
label = tk.Label(window, text="Binge Snake!")
label.pack()
 
# Start the stopwatch
start_stopwatch()
update_stopwatch()

# Display Snake

snake = Snake()
SnakeDisplay(snake)
# Run the window

window.update()

window.mainloop()

