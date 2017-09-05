# froggit step 05

# Now we need to kill the frog !
  
1. We need to listen to a mouse down event, we create a special function to listen for this, we need to create just above the update function.    

```
def on_mouse_down(pos):
```

3. This function is passed a parameter called pos - this is the position of the mouse at the time of mouse down. We determine if this position is within the frog, if it is we will call a new function called frog_hit
``` 
 def on_mouse_down(pos):
    if frog.collidepoint(pos):
        frog_hit()
```
4. We need to keep track if the frog is dead - so we need a new boolean variable is_alive, and set it to True initially. At the top of the code, with the other frog variable settings, add this   
```
 frog.is_alive = True  
```
5. Create a new function called frog_hit. Set the image of the frog to frog_dead, and set is_alive to False.  
```
 def frog_hit():  
    frog.is_alive = False
    frog.image = "frog_dead"
```
6. Modify the update function so that the code is only be executed if the is_alive flag is True.
We do not want to animate a dead frog!
```
def update():
    if frog.is_alive:
        frog_hop()
        frog.y -= 5
        if frog.y < 0:
            frog_reset()

```
 6. Test the code

 7. The frog should now appear dead, but we only want this to be temporary, we would like it to come back alive after a short period. We send an event that will wait one second and the reset the frog. At the end of  the frog_hit function add the following line:
```
  clock.schedule_unique(frog_reset,1.0)
```
We also need to set the is_alive flag back to True at the the beginning of the frog_reset function.  
```
frog.is_alive = True
```
8. Test the code





