import turtle

screen = turtle.Screen()
screen.setup(width=1200, height=700)  # SCREEN SIZE: width, height
screen.bgcolor("white")
screen.title("Mooseman Driving")

# Draw the black road lines
road = turtle.Turtle()
road.speed(0)
road.hideturtle()
road.penup()
road.color("black")
road.pensize(15)  # ROAD THICKNESS: higher = thicker

# TOP ROAD 1 - adjust position and angle
road.goto(-550, 50)  # STARTING POINT: (left/right, up/down)
road.setheading(0)   # ANGLE: 0=right, 90=up, -5=slightly down-right
road.pendown()
road.forward(420)     # LENGTH: how long the road is

# TOP ROAD 2
road.penup()
road.goto(-130, 50)  # STARTING POINT
road.setheading(-40)  # ANGLE
road.pendown()
road.forward(80)     # LENGTH

# BOTTOM ROAD 4
road.penup()
road.goto(120, -150)  # STARTING POINT
road.setheading(40)  # ANGLE
road.pendown()
road.forward(280)     # LENGTH

# BOTTOM ROAD 3
road.penup()
road.goto(-150, -150)  # STARTING POINT
road.setheading(0)  # ANGLE
road.pendown()
road.forward(280)     # LENGTH

# BOTTOM ROAD 2
road.penup()
road.goto(-260, -220)  # STARTING POINT
road.setheading(35)  # ANGLE
road.pendown()
road.forward(140)     # LENGTH

# BOTTOM ROAD 1
road.penup()
road.goto(-520, -220) # STARTING POINT
road.setheading(0)   # ANGLE
road.pendown()
road.forward(270)     # LENGTH

# Add the text at top
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, 240)  # TEXT POSITION: (left/right, up/down)
text.write("It look like you about to take us to find the moose man", 
           align="center", font=("Arial", 15, "normal"))  # FONT SIZE: 15
text.goto(0, 210)  # SECOND LINE POSITION
text.write("Who the hell is the moose man?", 
           align="center", font=("Arial", 15, "bold"))

# Create the car/arrow
car = turtle.Turtle()
car.hideturtle()     # Hide immediately so it doesn't appear at center
car.shape("square")  # SHAPE: "arrow", "turtle", "square", etc.
car.shapesize(stretch_wid=2, stretch_len=3)  # Shape SIZE: (width, length)
car.color("Blue")
car.pencolor("red")
car.pensize(15)  # LINE THICKNESS

# ===== THE DRIVING PATH =====

# START 80px ABOVE TOP ROAD 1
car.penup()
car.speed(0)     # Instant spawn
car.goto(-500, 130)  # 80px above TOP ROAD 1
car.speed(1)     # Back to slow for path animation
car.setheading(0)   # Face right initially
car.showturtle()     # Show it now that it's positioned
car.pendown()

# SEGMENT 1: Go right along above the top road
car.forward(400)     # Move right

# SEGMENT 2: Drop down diagonally to BOTTOM ROAD 4
car.right(30)        # Turn down-right
car.forward(150)     # First part of diagonal

# SEGMENT 2.1: Continue diagonal (creates another arrow)
car.left(8)        # Turn slightly up-left
car.forward(140)     # Second part of diagonal

# SEGMENT 2.2: Continue diagonal (creates another arrow)
car.right(30)        # Turn slightly up-right
car.forward(60)     # Second part of diagonal

# SEGMENT 2.3: Continue diagonal (creates another arrow)
car.right(80)        # Turn slightly up-right
car.forward(60)    # Second part of diagonal

# SEGMENT 2.4: Continue diagonal (creates another arrow)
car.right(20)        # Turn slightly up-right
car.forward(40)    # Second part of diagonal

# SEGMENT 3: Transition to BOTTOM ROAD 3
car.setheading(180)  # Turn left
car.forward(260)     # Move left

# SEGMENT 4: Drive along BOTTOM ROAD 3
car.left(20)         # Angle slightly
car.forward(100)     # Drive along BOTTOM ROAD 3

# SEGMENT 4.1: Drop down to BOTTOM ROAD 2
car.left(20)        # Turn down-left
car.forward(80)      # Drop to BOTTOM ROAD 2

# SEGMENT 5: Drive along BOTTOM ROAD 1 and go below
car.setheading(180)  # Face left
car.forward(150)     # Drive left on BOTTOM ROAD 1

screen.mainloop()
