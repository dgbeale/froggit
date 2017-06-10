WIDTH=640
HEIGHT=320

''' declarations '''
frog = Actor("frog1")
frog.pos = (320,HEIGHT + frog.height )
frog.frame = 1

def frog_hop():
    if frog.frame < 7:  
          frog.frame += 1  
    else:
          frog.frame = 1  
    frog.image = "frog" + str(frog.frame) 


''' game loop '''
# Event Handling


# Run Handling
def update():
    frog_hop()
    frog.y -= 5
    if frog.y < 0:
        frog.y = HEIGHT + frog.height


# Update the display
def draw():
    screen.fill((0,230,255))
    frog.draw()