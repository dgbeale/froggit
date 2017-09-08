# froggit step 07

# Now everything is working with 1 frog, let's now have 4 frogs
  
1. Lets modify our frog variable to frog1 and add 3 more. But they wil still use the image frog1 
```
frog1 = Actor("frog1")
frog2 = Actor("frog1")
frog3 = Actor("frog1")
frog4 = Actor("frog1")
```
2. After these variables, let's create an array (list) to store all our frogs
```
 frogs = [frog1,frog2,frog3,frog4]
```
3. We now need to change the code that previously used the frog variable to now user the array, using a **for** loop 
```
for frog in frogs:
    frog.pos = (0, -500)
    frog.frame = 1
    frog.is_alive = True
```
4. In the update function, add a for loop - and pass the frog variable to frog_hop function
```
for frog in frogs:
        if frog.is_alive:
            frog_hop(frog)
            frog.y -= 5
            if frog.y < 0:
                score -= 1
                frog_reset(frog)
```
5. Change frog_reset, frog_hop frog_hit functions to accept frog as a parameter
6. We now need to modify the logic within the mouse_down function. Currently it looks like this :
```
if frog.collidepoint(pos):
        frog_hit()
```
It checks whether the position of the mouse is within the frog.
So now, instead we will need to check each frog, unfortunately it's not possible to do this in a loop, so we need to replace the above with this :
```
if frog1.collidepoint(pos):
            frog_hit(frog1)
            clock.schedule_unique(frog1_reset,1.0)
    elif frog2.collidepoint(pos):
            frog_hit(frog2)
            clock.schedule_unique(frog2_reset,1.0)
    elif frog3.collidepoint(pos):
            frog_hit(frog3)
            clock.schedule_unique(frog3_reset,1.0)
    elif frog4.collidepoint(pos):
            frog_hit(frog4)
            clock.schedule_unique(frog4_reset,1.0)
```
7. As you can see above, each frog now has it's own reset function. So we need to add the following code, below the existing frog_reset function.
```
def frog1_reset(): frog_reset(frog1)
def frog2_reset(): frog_reset(frog2)
def frog3_reset(): frog_reset(frog3)
def frog4_reset(): frog_reset(frog4)
```
Each of the new reset functions, call the original frog_reset function, passing  the specific frog object as a variable.  
8. Please test the new code


