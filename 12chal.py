import turtle
data = open("12chal.txt").readlines()
#screen = turtle.TurtleScreenBase()
ship = turtle.Turtle()
ship.shape('turtle')
waypoint = turtle.Turtle()
test_data = ["F10",
"N3",
"F7",
"R90",
"F11"]
screen=turtle.getscreen()
data = [i.replace("\n","") for i in data]
def move_turtle(ship, waypoint, _str_command):
    command = _str_command[0]
    number = int(_str_command[1:])
    x,y = waypoint.position()
    angle = ship.towards(waypoint.position()+ship.position())
    ship.seth(angle)
    if command=='F':
        for i in range(number):
            xship,yship = ship.position()
            ship.setx(x+xship)
            ship.sety(y+yship)
    elif command =='N':
        waypoint.sety(y+number)
    elif command == 'S':
        waypoint.sety(y - number)
    elif command == 'E':
        waypoint.setx(x + number)
    elif command == 'W':
        waypoint.setx(x - number)
    elif command == 'L':
        waypoint.goto(waypoint.position().rotate(number))
    elif command == 'R':
        waypoint.goto(waypoint.position().rotate(-number))

print(ship.pos())
ship.speed('fastest')
waypoint.speed('fastest')
turtle.setworldcoordinates(-15000,-1000,3000,15000)
waypoint.goto(10,1)
from PIL import Image
for i,command in enumerate(data):
    move_turtle(ship, waypoint, command)
    cvs = screen.getcanvas()
    fname = 'turtleanim/'+'image'+'0'*(3-len(str(i)))+str(i)
    cvs.postscript(file=fname+'.eps')
    img = Image.open(fname+'.eps')
    img.save(fname+'.png', 'png')
    img.save(fname + '.jpg', 'JPEG')
print(ship.position())
x,y = ship.position()
print(abs(x)+abs(y))