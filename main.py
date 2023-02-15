import tkinter as tk
import pygame
# 2d Snake Game Board Dimensions

WIDTH = 1000
HEIGHT = 700
BODY_SIZE = 200
SPACE_SIZE = 20
BACKGROUND = "#5af5aa"
SNAKE = "#000000"
class Snake:
        def __init__(self):
            pygame.init()
         
            self.body_size = BODY_SIZE
            self.coordinates = []
            self.squares = []
            for i in range(0, BODY_SIZE):
                self.coordinates.append([20, 20])
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
         

# Create a new window
window = tk.Tk()

# Set the title of the window
window.title("Welcome to 2D snake game")

# Set the size of the window
canvas = tk.Canvas(window, bg=BACKGROUND,
                height=HEIGHT, width=WIDTH)
canvas.pack()
# Create a label widget and add it to the window
label = tk.Label(window, text="Binge Snake!")
label.pack()

snake = Snake()
SnakeDisplay(snake)
# Run the window
window.update()
window.mainloop()
