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





