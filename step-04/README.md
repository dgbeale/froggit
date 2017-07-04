# froggit step 04

# Let's now get the forg appearing in random places

1. Now we need the frog to appear in random places.  
2. We need to use the python library, random. At the top of the code, on the first line of your code add   
from random import randint
3. Create a new function called frog_reset, here we will randomly set the x and y co-ordinates.
4. randint reqires a range - min and maximum, for x the min should be 0 but we don't want the frog to appear half off the screen. For the max, we want to use the width of the screen - but take into account the width of the frog.  
  x = randint(0 + frog.width//2, WIDTH - frog.width//2)
5. For the y co-ordinate, 


