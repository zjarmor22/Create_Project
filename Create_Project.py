import time
import turtle
import pygame
from turtle import Turtle
from random import randint



name = input("Pick which turtle you think will win, red, orange, yellow, blue, purple, pink:")
if name == "red":
    print = ("You have chosen red turtle")
if name == "orange":
    print = ("You have chosen orange turtle")
if name == "yellow":
    print = ("You have chosen yellow turtle")
if name == "blue":
    print = ("You have chosen blue turtle")
if name == "purple":
    print = ("You have chosen purple turtle")
if name == "pink":
    print = ("You have chosen pink turtle")


#Window 

window = turtle.Screen()
window.title("Turtle Track")
turtle.bgcolor("green")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.goto(-160, 200)
turtle.write("TURTLE TRACK", font=("Times New Roman", 35, "bold" ))

#Finish Line - Geek Tutorials on YouTube

stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()

#End code from Geek Tutorials

turtle.color("white")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (133 - (i * square_size * 2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((166 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()

move = True
def position():
    global move
    if turtle.ycor() <= 150:
        move = False
    if turtle.xcor() >= 150:
        move = False
    if turtle.ycor() >= 150:
        move = False

#Turtle 1

turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("red")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-225, 125)
turtle1.pendown()

#Turtle 2

turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("yellow")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-225, 75)
turtle2.pendown()

#Turtle 3

turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("blue")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-225, 25)
turtle3.pendown()

#Turtle 4

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("pink")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-225, -25)
turtle4.pendown()

#Turtle 5

turtle5 = Turtle()
turtle5.speed(0)
turtle5.color("orange")
turtle5.shape("turtle")
turtle5.penup()
turtle5.goto(-225, -75)
turtle5.pendown()

#Turtle 6

turtle6 = Turtle()
turtle6.speed(0)
turtle6.color("purple")
turtle6.shape("turtle")
turtle6.penup()
turtle6.goto(-225, -125)
turtle6.pendown()

time.sleep(5)

for i in range(115):
    turtle1.forward(randint(1,6))
    turtle2.forward(randint(1,6))
    turtle3.forward(randint(1,6))
    turtle4.forward(randint(1,6))
    turtle5.forward(randint(1,6))
    turtle6.forward(randint(1,6))

