import turtle
import random

turtle.tracer(0, 0)
screen = turtle.Screen()
turtle.title("triangle hates circles")

howto = "\n                                         HOW TO PLAY" \
        "\nclick (don't hold it) W,A,S,D to move Front,Left,Down,Right respectively" \
        "\n                         Goal of the game is to dodge the circles" \
        "\n                                lick ENTER to start the game"
turtle.write(howto,align ="center", font=("Arial", 16, "normal"))

run = True
def start():
    print("start")
    main()

screen.listen()
screen.onkeyrelease(start, 'Return')
class game:
    def __init__(self, turtle):
        self.turtle = turtle

    def xcord(self):
        return self.turtle.xcor()

    def ycord(self):
        return self.turtle.ycor()

    def boundary(self):
        self.turtle.penup()
        self.turtle.goto(-350, 300)
        self.turtle.pendown()
        self.turtle.color("red")
        self.turtle.width(10)
        self.turtle.goto(350, 300)
        self.turtle.goto(350, -300)
        self.turtle.goto(-350, -300)
        self.turtle.goto(-350, 300)

    def ship(self, x, y):
        self.x = x
        self.y = y
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.color("red")
        self.turtle.begin_fill()
        for i in range(3):
            self.turtle.forward(50)
            self.turtle.left(120)
        self.turtle.end_fill()

    def enemy(self, x, y):
        self.x = x
        self.y = y
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.color("blue")
        self.turtle.begin_fill()
        self.turtle.circle(25)
        self.turtle.end_fill()

    def motion_down(self):
        self.x = self.turtle.xcor()
        self.y = self.turtle.ycor() - 5
        self.enemy(self.x, self.y)

    def motion_up(self):
        self.x = self.turtle.xcor()
        self.y = self.turtle.ycor() + 5
        self.enemy(self.x, self.y)

    def motion_right(self):
        self.x = self.turtle.xcor() + 5
        self.y = self.turtle.ycor()
        self.enemy(self.x, self.y)

    def motion_left(self):
        self.x = self.turtle.xcor() - 5
        self.y = self.turtle.ycor()
        self.enemy(self.x, self.y)

    def erase(self):
        self.turtle.clear()

turtle.shape("blank")
boundary = game(turtle.clone())
ship = game(turtle.clone())
enemy = game(turtle.clone())

f1 = game(turtle.clone())
f2 = game(turtle.clone())
d1 = game(turtle.clone())
d2 = game(turtle.clone())
l1 = game(turtle.clone())
l2 = game(turtle.clone())
r1 = game(turtle.clone())
r2 = game(turtle.clone())

enemy_front = [f1, f2]
enemy_down = [d1, d2]
enemy_left = [l1, l2]
enemy_right = [r1, r2]

for i in enemy_front:
    i.enemy(random.randint(-350, 350), random.randint(300, 500))
for i in enemy_left:
    i.enemy(random.randint(-500, -350), random.randint(-300, 300))
for i in enemy_right:
    i.enemy(random.randint(350, 500), random.randint(-300, 300))
for i in enemy_down:
    i.enemy(random.randint(-350, 350), random.randint(-500, -300))

ship_x = 0
ship_y = 0

enemy = game(turtle.clone())


def ship_right():
    global ship_x
    ship_x += 50
    ship.erase()
    ship.ship(ship_x, ship_y)

def ship_left():
    global ship_x
    ship_x -= 50
    ship.erase()
    ship.ship(ship_x, ship_y)

def ship_up():
    global ship_y
    ship_y += 50
    ship.erase()
    ship.ship(ship_x, ship_y)

def ship_down():
    global ship_y
    ship_y -= 50
    ship.erase()
    ship.ship(ship_x, ship_y)

score = 0
def score_display():
    global score
    score_board = "SCORE :"+str(score)
    print(score_board)
    turtle.goto(220,260)
    turtle.clear()
    turtle.write(score_board,align = "left", font=("Arial", 16, "normal"))
    score += 1

def gameover():
    global run
    run = False
    print("gameover")
    text =f"GAME OVER" \
          f"\n SCORE : {score}" \
          f"" \
          f"\n\nclick ENTER to retry"
    turtle.goto(0, 0)
    turtle.write(text,align ="center", font=("Arial", 25, "bold"))
    screen.listen()
    screen.onkeyrelease(retry, "Return")



def boundary_check():
    x = ship.xcord()
    y = ship.ycord()
    if x+50 >= 350 or x <= -350:
        gameover()
    if y+50 >= 300 or y <= -300:
        gameover()

def collison_check():
    x = ship.xcord()
    y = ship.ycord()

    for i in enemy_front:
        if x <= i.xcord()+25 and x >= i.xcord()-25 and y+40  >= i.ycord() and y+40 <= i.ycord() + 50:
            gameover()

    for i in enemy_left:
        if x <= i.xcord()+25 and x>= i.xcord() -25 and  y >= i.ycord() and y <= i.ycord() + 50:
            gameover()

    for i in enemy_right:
        if x + 50 <= i.xcord() + 50 and x + 50 >= i.xcord() - 25 and y >= i.ycord() and y <= i.ycord() + 50:
            gameover()

    for i in enemy_down:
        if x +25 <= i.xcord() + 25 and x + 25>= i.xcord() - 25 and y >= i.ycord() and y <= i.ycord() + 50:
            gameover()


def stop():
    run = False

def main():
    ship_left()
    while run:
        for i in enemy_front:
            i.erase()
            i.motion_down()
            if i.ycord() <= -300:
                i.enemy(random.randint(-350, 350), random.randint(300, 500))

        for i in enemy_left:
            i.erase()
            i.motion_right()
            if i.xcord() >= 350:
                i.enemy(random.randint(-500, -350), random.randint(-300, 300))

        for i in enemy_right:
            i.erase()
            i.motion_left()
            if i.xcord() <= -350:
                i.enemy(random.randint(350, 500), random.randint(-300, 300))

        for i in enemy_down:
            i.erase()
            i.motion_up()
            if i.ycord() >= 300:
                i.enemy(random.randint(-350, 350), random.randint(-500, -300))

        screen.listen()
        screen.onkeyrelease(stop, "Escape")
        screen.onkeyrelease(ship_right, 'd')
        screen.onkeyrelease(ship_left, 'a')
        screen.onkeyrelease(ship_up, 'w')
        screen.onkeyrelease(ship_down, 's')

        screen.update()
        score_display()
        collison_check()
        boundary_check()
        boundary.boundary()

def retry():
    global score
    score = 0
    for i in enemy_front:
        i.enemy(random.randint(-350, 350), random.randint(300, 500))
    for i in enemy_left:
        i.enemy(random.randint(-350, 350), random.randint(300, 500))
    for i in enemy_right:
        i.enemy(random.randint(-350, 350), random.randint(300, 500))
    for i in enemy_down:
        i.enemy(random.randint(-350, 350), random.randint(300, 500))
    global run
    run = True
    turtle.shape("blank")
    screen.clear()
    screen.tracer(0, 0)
    main()

turtle.mainloop()
