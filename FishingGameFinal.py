#imports
import turtle as trtl 
import random as rand
import math
import time
import threading

from functools import partial


wn = trtl.Screen()
wn.tracer(False)

#init variables
width, height = wn.window_width(), wn.window_height()
start_color = (0.6328, 0.87656, 0.91250)  # (154, 0, 254)
end_color = (0.10156, 0.5, 0.99218,)  # (221, 122, 80)
font_setup = "Verdana"
start_timer = 3
game_timer =  20
num_sandline = 9
startTimerBoolean = False
timer = 0
score = 0 

right_fish_shapes = ["left1.gif", "left2.gif", "left6.gif"]
left_fish_shapes = ["right2.gif", "right7.gif", "right8.gif"]
    

# trtl.Screen().register_shape("Fish2.gif")
# trtl.Screen().register_shape("Fish2.gif")
# trtl.Screen().register_shape("Fish1.gif")
# trtl.Screen().register_shape("Fish2.gif")
# trtl.Screen().register_shape("Fish3.gif")

left_fish = []
right_fish = []

#turtle setup
gradient = trtl.Turtle()
gradient.color(start_color)

gradient.penup()
gradient.goto(-width/2, height/2)
gradient.pendown()

sand = trtl.Turtle()
sand.hideturtle()
sand.penup()
sand.goto(-430, -300)
sand.pendown()
sand.left(25)
sand.fillcolor('#C2B280')

start_draw = trtl.Turtle()
start_draw.hideturtle()
start_draw.penup()
start_draw.goto(-40, 0)

timer = trtl.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(-400, 380)


#game function
def draw_backround():
    #Water
    deltas = []
    for i in range(3):
        delta = (end_color[i] - start_color[i]) / height
        deltas.append(delta)
        
    direction = 1
    for y in range(height//2, -height//2, -1):
        gradient.forward(width * direction)
        gradient.color([start_color[i] + deltas[i] * abs(y - height//2) for i in range(3)])
        gradient.sety(y)
        direction *= -1
        
    #Sand
    sand.begin_fill()
    for i in range(num_sandline):
        for i in range(5):
            sand.forward(10)
            sand.right(10)
            
        for i in range(5):
            sand.forward(10)
            sand.left(10)
        
    sand.setheading(270)
    sand.forward(180)
    sand.right(90)
    sand.forward(900)
    sand.right(90)
    sand.forward(180)

    sand.end_fill()
        
    
def countTimer():
    global game_timer
    while (game_timer > 0):
        time.sleep(1)
        #timer+=1
        game_timer -= 1
        #wn.update()
        
def handleClick(x, y):
    hitSomething = False
    
    for eachLeft in left_fish:
        xVal = eachLeft.xcor()
        yVal = eachLeft.ycor()
        
        if (
            (xVal - 200) <= x <= (xVal + 200)
            and
            (yVal - 200) <= y <= (yVal + 200)
            ):
            print("hit!!")
            
    if hitSomething:
        score += 1

def validationCheckX(x):
    return (-(wn.window_width() / 2) < x < (wn.window_width() / 2))

print(wn.window_height())
print(wn.window_width())

def generateY():
    return rand.randint(-((wn.window_height() / 2) - 200), ((wn.window_height()) / 2) - 150)

# i figured out the problem im a retard
# I AM N OT DOING THATH HSHI T IM FIXING UR CODWE AND THATS IT
def hitSomething(obj, x,y):
    global score
    score += 1
    
    obj.hideturtle()
    wn.update()

#Run
draw_backround()
#wn.onscreenclick(handleClick)

for i in left_fish_shapes:
    wn.register_shape(i)
    
    left_obj = trtl.Turtle(shape=i)
    
    left_obj.up()            
    
    left_obj.goto(-500, generateY())
    
    left_obj.onclick(partial(hitSomething, left_obj))

    left_fish.append(left_obj)

for i in right_fish_shapes:
    wn.register_shape(i)
    
    right_obj = trtl.Turtle(shape=i)
    
    right_obj.up()
    
    right_obj.goto(-500, generateY())
    
    right_obj.onclick(partial(hitSomething, right_obj))
    
    right_fish.append(right_obj)

# for i in left_fish:
#     i.onclick(i.hideturtle)

for i in range(start_timer):
    start_draw.write(str(start_timer), font=(font_setup, 100, "normal"))
    time.sleep(1)
    start_draw.clear()
    start_timer -= 1
    if (start_timer == 0):
        startTimerBoolean = not startTimerBoolean
        threading.Thread(target=countTimer, daemon=True).start()

while (game_timer >= 1):
    timer.clear()
    timer.write(str(game_timer), font=(font_setup, 15, "normal"))
        
    for eachLeft in left_fish:
        if (not eachLeft.isvisible()):
            continue
        eachLeft.forward(5 + rand.randint(10,30))
        if (eachLeft.xcor() > wn.window_width()):
            eachLeft.goto(-500, generateY())
    
    for eachRight in right_fish:
        if (not eachRight.isvisible()):
            continue
        eachRight.backward(5 + rand.randint(10,30))
        if (eachRight.xcor() < -wn.window_width()):
            eachRight.goto(500, generateY())
    
    wn.update()
            
    # for eachRight in right_fish:
        
    #     fish_pos = rand.randint(-250,450)    
       
    #     eachRight.penup()
    #     eachRight.goto(500, fish_pos)
    #     eachRight.showturtle()
        
    #     for f in range(200):
    #         eachRight.backward(10)
    #         timer.clear()
    #         timer.write(str(game_timer), font=(font_setup, 15, "normal"))
    #         wn.update()
         
            
print("Done!")