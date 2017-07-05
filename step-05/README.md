# froggit step 05

# Now we need to kill the frog !

1. Now we need the frog to appear in random places.  
2. We need to listen to a mouse down event, we create a special function to listen for this, we need to create just above the update function.    
def on_mouse_down(pos):
3. This function is passed a parameter call pos - this is  the position of the mouse at the time of mouse down. We determine if this position is within the frog, if it is we will call a new function called forg_hit
 def on_mouse_down(pos):
    if frog.collidepoint(pos):
        frog_hit()
4. We need to keep track if the frog is dead - so we need a new boolean variable is_alive, and set it to True initially. At the top of the code, with the other frog variable settings.  
 frog.is_alive = True  

4. Create a new function called frog_hit. Set the image of the frog to frog_dead, and set is_alive to False.  
 def frog_hit():  





