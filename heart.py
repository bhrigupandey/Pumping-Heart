import turtle
import math
import random

# Set up the screen canvas
screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Glowing Particle Star Heart")
screen.tracer(0)  # Turns off automatic screen updates for smooth animation

# List to store the pre-calculated coordinates for the glowing stars
star_positions = []

# Parametric heart equations
def heart_x(t):
  return 16 * math.sin(t) ** 3

#heart shape
def heart_y(t):
  return (
      13 * math.cos(t)
      - 5 * math.cos(2 * t)
      - 2 * math.cos(3 * t)
      - math.cos(4 * t)
  )

random.seed(40)  # Keeps stars locked to their relative positions while scaling 

# Color palette to create a "glowing neon red" look
#neon_colors = ["#ff0033", "#ff3355", "#ff6688", "#ff99aa", "#ffffff"]

# Generate dots for a dense, starry galaxy effect
for _ in range(10000):
    t_rand = random.uniform(0, 2 * math.pi)
    
    # Power Scaling Trick (0.4 keeps it dense at the edges but blends smoothly)
    edge_weight = random.uniform(0, 1) ** 0.4
    scale = edge_weight * 14.5
    
    tx = heart_x(t_rand) * scale
    ty = heart_y(t_rand) * scale
    
    # Give outer stars a brighter/whiter color to mimic a neon glow edge
    if edge_weight > 0.85:
        color = random.choice(["#ffffff", "#ffb3d9", "#ff66cc"]) # Glowing bright edge
    else:
        color = random.choice(["#ff00a0", "#ff40b3", "#b30071"]) # Deep pink inner mist
        
    # Varied sizes to make them look like distant twinkling stars
    star_size = random.choice([1, 2, 3])
    
    star_positions.append((tx, ty, star_size, color))

# Star Animation Turtle 
star_pen = turtle.Turtle()
star_pen.hideturtle()
star_pen.speed(0)

#Pumping Animation Loop
base_scale = 12
angle = 0  

while True:
    # Clear the previous animation frame
    star_pen.clear()

    # Create the double-beat pulse rhythm
    pulse = math.sin(angle)
    if pulse > 0:
        scale_factor = base_scale + (pulse**1) * 1.8
    else:
        scale_factor = base_scale + (pulse**2) * 5.0

    angle += 5.0 # Controls heartbeat speed
    ratio = scale_factor / base_scale

    # Draw all glowing stars
    for tx, ty, size, color in star_positions:
        star_pen.penup()
        star_pen.goto(tx * ratio, ty * ratio)
        star_pen.pendown()
        
        star_pen.color(color)
        star_pen.dot(size)

    # Push the fully drawn starry frame to the screen instantly
    screen.update()
