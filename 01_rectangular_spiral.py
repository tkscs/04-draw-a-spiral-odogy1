import turtle

"""
Make a rectangular spiral (see the README.md for an example)
"""

### YOUR CODE STARTS HERE
x = 50
for y in range(1,100):
    turtle.forward(x * y)
    turtle.right(90)
    turtle.forward(x * y)
    turtle.right(90)

### YOUR CODE ENDS HERE

turtle.exitonclick()