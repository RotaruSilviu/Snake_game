from turtle import Turtle

### Variabile constante, acestea nu se vor schimba niciodată doar daca vrem vreodată sa modificam ceva in jocul nostru.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# TODO 1: Snake body.
class Snake:
    ### Definim clasa.
    def __init__(self):
        ### Lista in care se adauga fiecare segment din sarpe. Primul segment fiind capul.
        self.segments = []
        ### Chemam functia de mai jos pentru a crea un sarpe din 3 segmente initial.
        self.create_snake()
        ### Capul sarpelui.
        self.head = self.segments[0]

    def create_snake(self):
        ### Cream sarpele, forma, culoarea, si pozitia de inceput si le adaugam la lista de segmente.
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)


    def add_segment(self, positions):
        new_segment = Turtle(shape="circle")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Add a segment to the snake.
        self.add_segment(self.segments[-1].position())

    # TODO 2: Move the Snake.
    def move(self):
        ### Ca sa putem muta sarpele fara sa arate ciudat pe ecran trebuie sa il mutam in felul in care ultimul segment
        # sa ia locul penultimului segment si tot așa in felul acesta ar arata bine pe ecran.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            ### Aflam coordonatele segmentul precedent si mutam ultimul segment in locul celui de înaintea lui.
            # Facem acest lucru cu toate segmentele ulterioare panas ajungem la cap.
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # TODO 3: Control the snake.
    ### Avand in vedere ca sarpele nu se poate intoarce 180 de grade in spate trebuie sa avem un if statement
    # ca sa nu se intample acest lucru
    ### Cu functia heading aflam directia care merge si cu setheading o sa setam directia in care merge.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
