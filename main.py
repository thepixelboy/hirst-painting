# TODO: Paint a pattern of 10 by 10 circles
# TODO: Every circle should be of 20 in size
# TODO: Space the circles around 50 paces of each other
import turtle as t
import random

color_list = [(226, 231, 236), (57, 106, 148), (224, 201, 110), (133, 85, 59), (222, 142, 65), (196, 145, 171), (224, 234, 230), (234, 225, 203), (144, 179, 203), (138, 82, 105), (210, 91, 67), (187, 79, 120), (134, 182, 136), (69, 104, 89), (236, 223, 231), (65, 155, 90), (133, 133, 75), (49, 155, 194), (183, 192, 201), (214, 178, 191), (22, 68, 112), (21, 59, 95), (175, 202, 181), (114, 124, 150), (227, 176, 167), (158, 205, 214), (70, 59, 48), (72, 65, 53), (124, 45, 40), (110, 48, 58), (54, 71, 66), (46, 67, 59)]
dots = 101
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

def random_color():
  """Selects a color ramdomly from the color_list"""
  return random.choice(color_list)

# Hiding the turtle, avoiding it to pait lines as we move and changing the position
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Drawing circles
for dot in range(1, dots):
  tim.dot(20, random_color())
  tim.forward(50)

  if dot % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()