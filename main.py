import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = 'Shoot the Alien'

message = 'Click to Start'
alien = Actor('alien')
alien.pos = 50, 50

def draw():
    screen.clear()
    screen.fill(color = (128, 0, 0))
    alien.draw()
    screen.draw.text(message, center = (250, 30), fontsize = 30)

def place_alien():
    alien.x = random.randint(50, WIDTH-50)
    alien.y = random.randint(50, HEIGHT-50)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = 'Good Shot!'
        place_alien()
    else:
        message = 'Miss! Try again!'
place_alien()


pgzrun.go()