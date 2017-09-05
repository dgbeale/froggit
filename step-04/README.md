# froggit step 04

# Let's now get the frog appearing in random places

1. Now we need the frog to appear in random places.  
2. We need to use the python library, random. At the top of the code, on the first line of your code add

```   
from random import randint
```
3. Create a new function called frog_reset, here we will randomly set the x and y co-ordinates.
4. randint requires a range - min and maximum, for x (horizontal position) the min should be 0 but we don't want the frog to appear half off the screen. For the max, we want to use the width of the screen - but take into account the width of the frog.    
```
  x = randint(0 + frog.width//2, WIDTH - frog.width//2)
```
5. For the y co-ordinate (the vertical position), we will also create a a random value. The min should be the HEIGHT of the screen, the max can be a large value so that the frog can seem to appear at different times, we can use frog.height * 2
6. So the frog_reset function should look like this  

```
def frog_reset():   
    x = randint(0 + frog.width // 2, WIDTH - frog.width // 2)  
    y = randint(HEIGHT + frog.height // 2, HEIGHT * 2)  
    frog.pos = (x,y)  

```
7. We now need to call the reset method when the frog goes off the screen. In the update method, it should look like this
```
  if frog.y < 0:
        frog_reset()
```
8. Change the initial frog position to be off the screen
```
frog.pos = (0, -500)
```
9. Now test the code




