from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakes = []
        snake1 = Turtle()
        self.snakes.append(snake1)
        snake2 = Turtle()
        self.snakes.append(snake2)
        snake3 = Turtle()
        self.snakes.append(snake3)
        self.initialize()
        self.direction = 0



    def add_snake(self):
        new_snake = Turtle()
        new_snake.penup()
        new_snake.color("white")
        new_snake.shape("square")
        new_snake.setpos(self.snakes[-1].position())
        self.snakes.append(new_snake)


    def initialize(self):
        x = 0
        for creatures in self.snakes:
            creatures.penup()
            creatures.color("white")
            creatures.shape("square")
            creatures.setpos(x, 0)
            x -= 20


    def up(self):
        if self.direction != DOWN:
            self.direction = UP

    def down(self):
        if self.direction != UP:
            self.direction = DOWN

    def right(self):
        if self.direction!= LEFT:
            self.direction = RIGHT

    def left(self):
        if self.direction != RIGHT:
            self.direction = LEFT



    def move(self):
        for creature_num in range(len(self.snakes) -1, 0, -1):
            new_x = self.snakes[creature_num -1].xcor()
            new_y = self.snakes[creature_num -1].ycor()
            self.snakes[creature_num].goto(new_x, new_y)
        self.snakes[0].setheading(self.direction)
        self.snakes[0].forward(MOVE_DISTANCE)