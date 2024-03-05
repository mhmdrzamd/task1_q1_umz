# mohammadreza mohammadi   40113260281818

import turtle
wn = turtle.Screen()
my_turtle = turtle.Turtle()
wn.setup(width=800 , height=600)
wn.title('turtle umz question')

wn.bgcolor('light blue')

my_turtle.pencolor(input('enter your fave color for square: '))
my_turtle.pensize(5)
num = int(input('enter your fave size for each side of square: '))

for i in range(4):

    my_turtle.forward(num)
    my_turtle.right(90)




wn.mainloop()