from random import randint


WIDTH=640
HEIGHT=320

''' declarations '''
frog = Actor("frog1")
frog.pos = (0, -500)
frog.frame = 1
frog.is_alive = True
score = 1

def frog_hop():
    if frog.frame < 7:  
          frog.frame += 0.5 
    else:
          frog.frame = 1
    frog.image = "frog" + str(int(frog.frame))
  


''' game loop '''
def frog_reset():
    frog.is_alive = True
    x = randint(0 + frog.width // 2, WIDTH - frog.width // 2)
    y = randint(HEIGHT + frog.height // 2, HEIGHT * 2)
    frog.pos = (x,y)

def on_mouse_down(pos):
    if frog.collidepoint(pos):
        frog_hit()
        
def frog_hit():
    global score
    score += 1
    frog.is_alive = False
    frog.image = "frog_dead"
    clock.schedule_unique(frog_reset,1.0)

def update():
    global score
    if frog.is_alive:
        frog_hop()
        frog.y -= 5
        if frog.y < 0:
            score -= 1
            frog_reset()


# Update the display
def draw():
    global score
    screen.fill((0,230,255))
    frog.draw()
    screen.draw.text(str(score), (WIDTH//2 - 20 , 0))