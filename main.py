import tkinter as tk
import random
# 2d Snake Game Board Dimensions
WIDTH = 1000
HEIGHT = 700
BACKGROUND = "#5AF5AA"
SPEED = 200
FOOD = "#FFFFFF"
BODY_SIZE = 2
SPACE_SIZE = 20
SNAKE = "#000000"
# Create Snake
class Snake:
        def __init__(self):
            self.body_size = BODY_SIZE
            self.coordinates = []
            self.squares = []
            for i in range(0, BODY_SIZE):
                self.coordinates.append([0, 0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(
                    x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                        fill=SNAKE, tag="snake")
                self.squares.append(square)
  # Class to design the food
class Food:
    def __init__(self):
        x = random.randint(0,
                (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0,
                (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y +
                        SPACE_SIZE, fill=FOOD, tag="food")
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
 # Function to check the next move of snake
def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE,
                y + SPACE_SIZE, fill=SNAKE)
    snake.squares.insert(0, square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Points:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)
# Function to control direction of snake
def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= WIDTH:
        return True
    elif y < 0 or y >= HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False
# Function to control everything
def game_over():
    canvas.delete()
    canvas.create_text(canvas.winfo_width()/2,
                    canvas.winfo_height()/2,
                    font=('consolas', 70),
                    text="GAME OVER", fill="red",
                    tag="gameover")


# Giving title to the gaming window
window = tk.Tk()
window.title("2D Binge Snake")
score = 0
direction = 'down'
####################
timer_text = canvas.create_text(50, 10, text="Time: 0s", fill="black", font=("Arial", 16, "bold"))
# Define a function to start the stopwatch
def start_stopwatch():
    global timer_running
    timer_running = True
# Define a function to stop the stopwatch
def stop_stopwatch():
    global timer_running
    timer_running = False
start_stopwatch()
update_stopwatch()
snake = Snake()
food = Food()
next_turn(snake, food)
window.mainloop()