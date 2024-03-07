from tkinter import *
import random

width = 700
height = 700
speed = 70
size = 50
body = 3
snake_colour = "#00FF00"
food_colour = "#FF0000"
bg_colour = "#000000"
u= (width / size) - 1
v= (height / size) - 1

class Snake:

    def __init__(self):
        self.body_size = body
        self.coordinates = []
        self.squares = []

        for i in range(0,body):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + size, y + size, fill= snake_colour, tags="snake")
            self.squares.append(square)




class Food:

        def __init__(self):
            #(width / size) - 1
            #(height / size) - 1
            x = random.randint(0, u) * size
            y = random.randint(0, v) * size

            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + size, y + size, fill=food_colour, tags="food")


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction =="up":
        y -= size
    elif direction =="down":
        y += size
    elif direction =="left":
        x -= size
    elif direction =="right":
        x += size

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + size, y + size, fill=snake_colour)

    snake.squares.insert(0, square)

    if x== food.coordinates[0] and y == food.coordinates[1]:

        global score
        score += 1
        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    window.after(speed, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction

    elif new_direction == "right":
        if direction != "left":
            direction = new_direction

    elif new_direction == "up":
        if direction != "down":
            direction = new_direction

    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

def check_collision(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x>= width:
        return True

    elif y < 0 or y >= height:
        return True

    for body in snake.coordinates[1:]:
        if x == body[0] and y == body[1]:
            print("GAME OVER")
            return True

    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tags="gameover")


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score:{}".format(score), font=('consolas',40))
label.pack()

canvas = Canvas(window, bg=bg_colour, height=height,width=width)
canvas.pack()

window.update()

width = window.winfo_width()
height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))

window.geometry(f"{width}x{height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
