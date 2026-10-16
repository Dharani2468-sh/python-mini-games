from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, goto):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(goto)
        self.shapesize(stretch_wid=5,stretch_len=1)

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(),new_y)















# STARTING_POSITION = [(-360, -20), (-360, 0), (-360, 20)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
#
# class Paddle(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.segments = []
#         self.create_paddle()
#         self.head = self.segments[0]
#
#     def create_paddle(self):
#         for position in STARTING_POSITION:
#             new_segment = Turtle("square")
#             new_segment.penup()
#             new_segment.color("white")
#             new_segment.goto(position)
#             self.segments.append(new_segment)
#
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
#     def up(self):
#         self.head

