from turtle import *

#square
begin_fill()
color("cyan")
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
end_fill()

#door

begin_fill()
color("green")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


#roof
penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#1st windows
penup()
goto(180, 180)
pendown()

color("brown")
right(60)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
back(25)
left(90)
forward(25)
back(50)

#2nd window
penup()
goto(20, 180)
pendown()

forward(60)
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(30)
right(90)
forward(50)
back(25)
right(90)
forward(30)
back(60)




exitonclick()