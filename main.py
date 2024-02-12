from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
### Nu se mai afișează animatia.
screen.tracer(0)

### Chemam clasa Snake din fisierul aferent.si Clasa Food. Si clasa Scoreboard.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    ### Se foloseste impreuna cu tracer pentru ca updata interfata si a aparea snake ul pe ecran.
    screen.update()
    ### Viteza cu care se misca sarpele.
    time.sleep(0.1)
    snake.move()
    ### in cazul in care capul sarpelui se apropie la mai putin de 15 pixeli de mancare,
    # atunci mancarea isi schimba pozitia.

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        ### Cu functia increase score din clasa scoreboard afisam pe ecran scorul si il marim in concordanta.
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    ### Cu Slicing omitem primul element din lista segments.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
