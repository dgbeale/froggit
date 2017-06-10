# froggit step 03

# We can now start applying some animation to the frog

1. To control the animation, we create a new variable call frame, and set to 1   
    frog.frame = 1  
2. Create a new function that make the frog 'hop'.  
Increate the frame value each time the funcation is called.  
  def frog_hop:  
     frog.frame += 1  
Use this value, to retrireve  a different image of the frog (we have 7 frog images)  
     frog.image = "frog" + str(frog.frame)  
But because we only have 7 images, we should reset back to 1 after 7  
     if frog.frame < 7:  
        frog.frame += 1  
     else
        frog.frame = 1  
     frog.image = "frog" + str(frog.frame)  
3. Now we need to call this function, so add this to the first line in the update function  
     frog_hop()
4. Noe test the code.
5. Once this is running successfully, you will see that it's a bit too fast, we need to slow it down.
6. So, in our frog_hop section, instead of incrementing the frame by 1, let's increment by 0.5  
  frog.frame += 0.5
7. But we have now image with '.5' in the name, so we'll add an int function when using the frame value.  
  frog.image = "frog" + str(int(frog.frame))
8. Now we need the frog to appear in random places.  
9. We need to use the python library, random
At the top of the code, add   
from random import randint
10. Create a new function called frog_reset, here we will randomly set the x and y co-ordinates.
11. randint requeres a range - min and maximum, for x the minimum should be 0 but we don't want the frog to appear half off the screen. For the max, we want to use the width of the screen - but take into account the width of the frog.  
  x = randint(0 + frog.width//2, WIDTH - frog.width//2)
12. For the y co-ordinate, 
 




