import turtle
#import twilio
def draw_square(some_turtle):
    some_turtle.speed(15)
    some_turtle.color("yellow");
    for i in range(0,4):
        some_turtle.forward(35);
        some_turtle.right(90);

def draw_triangle():
    brad  =  turtle.Turtle();
    brad.shape("circle")
    brad.color("blue");
    brad.speed(5)
    for i in range(0,3):
        brad.forward(35);
        brad.right(120);
    
def draw_circle():
    brad  =  turtle.Turtle();
    brad.shape("arrow")
    brad.color("white");
    brad.circle(100)

    
def draw_shape():
    window = turtle.Screen();
    window.bgcolor("red");
    brad = turtle.Turtle();
    for i in range(1,21):
        draw_square(brad)
        brad.right(18)
    #draw_triangle()
    #draw_circle()
    window.exitonclick();
    
    
draw_shape()
#print(twilio.__version__)

