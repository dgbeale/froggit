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
    frog.image = "frog" + str(int(frog.frame))
  

''' game loop '''
# Event Handling


# Run Handling
def update():
    frog_hop()
    if frog.image == 'frog7':
        frog.y += 4
    else:
        frog.y -= 4
    if frog.y < 0:
        frog.y = HEIGHT + frog.height


# Update the display
def draw():
    screen.fill((10,0,150))
    frog.draw()