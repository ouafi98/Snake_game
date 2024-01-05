from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # self.head.color("red")

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)   
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())


    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto( self.segments[seg_num-1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    
    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
