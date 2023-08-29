from turtle import Turtle, Screen
import random

screen = Screen()
screen_height = screen.window_height()
screen_width = screen.window_width()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-int(((screen_width/2)-20)), int((screen_width/2)-20))
        random_y = random.randint(-int(((screen_height/2)-20)), int((screen_height/2)-20))
        self.goto(random_x, random_y)
