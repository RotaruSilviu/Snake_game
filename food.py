from turtle import Turtle
import random


### Turtle este superclass si incercam ca clasa food sa mosteneasca trasaturile ei.
class Food(Turtle):
    ### Clasa food a mostenit toate caracteristicile clasei Turtle si cream mancarea.
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        ### Chemam functia refresh ca bucata de mancare odata cea fost atinsa sa se miste in alta parte.
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, +280)
        random_y = random.randint(-280, +280)
        self.goto(random_x, random_y)
