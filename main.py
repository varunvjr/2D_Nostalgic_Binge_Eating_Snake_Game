import tkinter as tk
import random
import pygame
# 2d Snake Game Board Dimensions
WIDTH = 1000
HEIGHT = 700
BACKGROUND = "#5AF5AA"
SPEED = 200
FOOD = "#FFFFFF"
BODY_SIZE = 2
SPACE_SIZE = 20
SNAKE = "#000000"
score = 0

# Create Snake
class Snake:
        def __init__(self):
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("background.mp3")
            pygame.mixer.music.play(-1)
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
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Endgame.mpeg")
    pygame.mixer.music.play(-1)
    canvas.delete()
    global timer_running
    timer_running = False
    canvas.create_text(canvas.winfo_width()/2,
                    canvas.winfo_height()/2,
                    font=('consolas', 70),
                    text="GAME OVER", fill="red",
                    tag="gameover")
    
    canvas.create_text(canvas.winfo_width()/2,
                    canvas.winfo_height()/3,
                    font=('consolas', 50),
                    text="Your Score: {}".format(score), fill="green",
                    tag="score")
    


# Giving title to the gaming window
window = tk.Tk()
window.title("2D Binge Snake")

direction = 'down'

# Display of Points Scored in Game
label = tk.Label(window, text="Points:{}".format(score),
            font=('consolas', 20))
label.pack()
canvas = tk.Canvas(window, bg=BACKGROUND,
                height=HEIGHT, width=WIDTH)
canvas.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>',
            lambda event: change_direction('left'))
window.bind('<Right>',
            lambda event: change_direction('right'))
window.bind('<Up>',
            lambda event: change_direction('up'))
window.bind('<Down>',
            lambda event: change_direction('down'))
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