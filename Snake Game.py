import turtle 
import time 
import random
# Config
WIDTH, HEIGHT = 600, 600
DELAY = 100
GRID = 20

# Screen 
wn = turtle.Screen() 
wn.title("Snake (turtle)") 
wn.bgcolor("black") 
wn.setup(width=WIDTH, height=HEIGHT) 
wn.tracer(0)

# Snake head 
head = turtle.Turtle() 
head.shape("square") 
head.color("lime") 
head.penup() 
head.goto(0, 0) 
head.direction = "stop"

# Snake body segments 
segments = []

# Food 
food = turtle.Turtle() 
food.shape("circle") 
food.color("red") 
food.penup() 
food.goto(0, 100)

# Score display 
score = 0 
high_score = 0 
pen = turtle.Turtle() 
pen.hideturtle() 
pen.speed(0) 
pen.color("white") 
pen.penup() 
pen.goto(0, HEIGHT//2 - 40) 
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 16, "normal"))

def update_score(): 
    pen.clear() 
    pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 16, "normal"))



# Controls 
def go_up(): 
    if head.direction != "down": 
        head.direction = "up"

def go_down(): 
    if head.direction != "up": 
        head.direction = "down"

def go_left(): 
    if head.direction != "right": 
        head.direction = "left"

def go_right(): 
    if head.direction != "left": 
        head.direction = "right"

wn.listen() 
wn.onkeypress(go_up, "Up") 
wn.onkeypress(go_down, "Down") 
wn.onkeypress(go_left, "Left") 
wn.onkeypress(go_right, "Right")

def move(): 
    x, y = head.xcor(), head.ycor() 
    if head.direction == "up": 
        head.sety(y + GRID) 
    elif head.direction == "down":
        head.sety(y - GRID) 
    elif head.direction == "left": 
        head.setx(x - GRID) 
    elif head.direction == "right": 
        head.setx(x + GRID)

def random_food_pos():
     # Place food aligned to the grid within bounds 
     max_x = (WIDTH//2 - GRID) 
     max_y = (HEIGHT//2 - GRID) 
     fx = random.randrange(-max_x, max_x + 1, GRID) 
     fy = random.randrange(-max_y, max_y + 1, GRID) 
     return fx, fy

def reset_game():
     global score, segments 
     time.sleep(0.6) 
     head.goto(0, 0) 
     head.direction = "stop" 
     for seg in segments: 
         seg.goto(1000, 1000) 
     segments.clear() 
     score = 0 
     update_score() 
     food.goto(*random_food_pos())

# Main loop 
while True: 

    wn.update() 
    # Check wall collision 
    half_w, half_h = WIDTH//2, HEIGHT//2
    if (head.xcor() > half_w - GRID or head.xcor() < -half_w + GRID or head.ycor() > half_h - GRID or head.ycor() < -half_h + GRID): 
        reset_game()
    
    # Check food collision 
    if head.distance(food) < GRID / 2:
        # Move food 
        food.goto(*random_food_pos()) 
        # Add segment 
        new_seg = turtle.Turtle() 
        new_seg.shape("square") 
        new_seg.color("green") 
        new_seg.penup() 
        segments.append(new_seg)

        # Update score 
        score += 10 
        if score > high_score: 
            high_score = score 
        update_score()

    # Move segments from tail to front 
    for i in range(len(segments) - 1, 0, -1): 
        x = segments[i - 1].xcor() 
        y = segments[i - 1].ycor() 
        segments[i].goto(x, y)

    if segments: 
        segments[0].goto(head.xcor(), head.ycor())
    
    move() 
    # Check self collision
    for seg in segments: 
        if seg.distance(head) < GRID / 2: reset_game() 
    
    time.sleep(DELAY / 1000.0)
    