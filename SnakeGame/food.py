from turtle import Turtle
import  random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.reset_food()

    def reset_food(self):
        random_x = random.randrange(-280,280)
        random_y = random.randrange(-280,280)
        self.goto(random_x,random_y)



















# class Animal:
#     def __init__(self):
#         self.eyes = 2
#     def breathe(self):
#         print("Inhale, exhale")
#
# class fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater.")
#
# nimo = fish()
# nimo.breathe()