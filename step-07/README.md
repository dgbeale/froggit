# froggit step 07

# Now everything working with 1 frog, let's now have 4 frogs
  
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
4. In the update method, add a for loop - and pass the frog variable to forg_hop function
```
for frog in frogs:
        if frog.is_alive:
            frog_hop(frog)
            frog.y -= 5
            if frog.y < 0:
                score -= 1
                frog_reset()
```



