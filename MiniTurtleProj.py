import turtle
def draw_Upper_triangle(brad):
    brad.speed(10)
    for i in range(0,3):
        brad.forward(350);
        if(i!=2):
            brad.left(120);

def draw_lower_triangle(brad,length):
    brad.shape("circle")
    brad.color("blue");
    brad.speed(5)
    for i in range(0,3):
        brad.forward(length);
        if(i!=2):
            brad.right(120);

            
def draw_lower_triangle_right_side(brad,length):
     brad.shape("circle")
     brad.color("blue");
     brad.speed(5);
     for i in range(0,3):
        brad.forward(length);
        if(i!=2):
            brad.left(120);

def draw_lower_base_triangle(brad,length):
    for i in range(0,3):
        brad.forward(length);
        if(i!=2):
            brad.right(120);
    
                        

#def draw_mini_Triangle(brad,length):
    
      

brad = turtle.Turtle();
wn = turtle.Screen();
wn.bgcolor("lightgreen");
length = 350
draw_Upper_triangle(brad);
brad.right(180)
brad.forward(length/2);
brad.right(60)
draw_lower_triangle(brad,length/2)
brad.right(60)
brad.forward(length/4)
brad.right(60)
draw_lower_triangle(brad,length/4)
brad.left(120)
brad.forward(length/2)
brad.left(120)
draw_lower_triangle(brad,length/4)
brad.right(60)
brad.forward(3*length/4)
brad.left(180)
for i in range(0,4):
    if(i==0):
        brad.forward(length/8)
        brad.left(120)
    else:
        brad.left(120)
        brad.forward(length/4)
        brad.left(120)
    draw_lower_triangle(brad,length/8)
brad.right(60)
brad.forward(7*length/8)
brad.right(120)
brad.forward(3*length/4)
brad.right(120)
draw_lower_triangle_right_side(brad,length/4)
brad.left(60)
brad.forward(3*length/4)
brad.right(180)
for i in range(0,3):
      if(i==0):
        brad.forward(3*length/8)
        brad.right(120)
      else:
        brad.right(120)
        brad.forward(length/4)
        brad.right(120)
      draw_lower_triangle_right_side(brad,length/8)
brad.right(120);
brad.forward(length/8);
brad.right(120);
brad.forward(3*length/8);
brad.right(60)
draw_lower_base_triangle(brad,length/8)
brad.right(60);
brad.forward(length/4);
brad.right(60)
draw_lower_base_triangle(brad,length/8)
wn.exitonclick();






