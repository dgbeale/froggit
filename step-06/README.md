# froggit step 06

# Now we need to keep score, adding when hit, subtracting when we miss
  
1. Let's create a variable called score. We will initially set it to 1 
```
score = 1
```
2. Everytime we hit the frog, increment score. In frog_hit add :
```
 score += 1
```
3. Everytime the frog goes off the screen, decrement the score. This is in the update function, before the call to frog_reset.
```
score -= 1
```
4. Now we need to display it on the screen. In the draw function, after frog.draw() :  
```
screen.draw.text(str(score), (WIDTH//2 - 20 , 0))
```

