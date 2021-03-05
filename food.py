from turtle import Turtle
import random

COLOR_LIST = ["yellow", "blue", "pink", "green", "red", "purple"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color(random.choice(COLOR_LIST))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLOR_LIST))
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)