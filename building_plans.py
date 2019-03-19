from turtle import *

# Set Up Canvas
title("Building Plans")
bgcolor("white")

#Church Bottom
def church_bottom():
    #Creating Room
    penup()
    pencolor('black')
    goto(-200,-200)
    pendown()
    fillcolor('darkslateblue')
    begin_fill()
    forward(150)
    left(90)
    forward(50)
    left(90)
    forward(150)
    left(90)
    forward(50)
    end_fill()
    penup()
    
    #Creating the Door
    goto(-110,-200)
    pencolor('black')
    fillcolor('brown')
    pendown()
    begin_fill()
    left(90)
    forward(25)
    left(90)
    forward(35)
    left(90)
    forward(25)
    left(90)
    forward(35)
    end_fill()
    penup()
    goto(-105,-185)
    pencolor('gold')
    dot(5)
    penup()

#Run Bottom
church_bottom()


#Church Middle

def church_middle():
    fillcolor('darkslateblue')
    pencolor('black')
    goto(-200,-150)
    pendown()
    begin_fill()
    left(90)
    forward(150)
    left(90)
    forward(50)
    left(90)
    forward(150)
    left(90)
    forward(50)
    end_fill()
    penup()
    
church_middle()

#Church Roof
    

def church_roof():
    #Creating Triangle
    fillcolor('slategray')
    pencolor('black')
    goto(-200,-100)
    pendown()
    begin_fill()
    left(90)
    forward(150)
    left(120)
    forward(150)
    left(120)
    forward(150)
    left(125)
    end_fill()
    
    #Create Cross
    penup()
    fillcolor('yellow')
    setheading(90)
    forward(108)
    right(82)
    forward(68)
    setheading(90)
    pendown()
    begin_fill()
    right(90)
    forward(16)
    left(90)
    forward(25)
    right(90)
    forward(10)
    left(90)
    forward(16)
    left(90)
    forward(10)
    right(90)
    forward(16)
    left(90)
    forward(16)
    left(90)
    forward(16)
    right(90)
    forward(10)
    left(90)
    forward(16)
    left(90)
    forward(10)
    right(90)
    forward(25)
    end_fill()
    pendown()

church_roof()



# Close Gracefully
hideturtle()
done()



