# froggit step 02

# This steps will get the frog moving across the screen

1. If not already - Start Python IDLE
2. If not already - Start a Windows Command Line session - position IDLE and Command next to each other
3. Within the command line session, navigate to the folder created earlier (cd  _HOME_/froggit)
4. Download the images folder from this githib directory to a folder called 'images'  (thanks to www.gameartguppy.com)
5. Comment the code to show different areas :  
''' Declarations '''    underneath the two variables
''' Game Loop '''   A few lines underneath

6. Declare variable for the frog within declararions section - this is a special type called Actor. We will pass it the name of the frog image we require.
```  
    frog = Actor("frog1")
```
7. Set the initial position of the frog underneath.  
``` 
    frog.pos(320,100)
```    
8. Draw the frog, as the last line within the draw function.  
```
    frog.draw() 
```    
9. Test the code
10. Now we need to animate the frog, create a new function called update (this is called by PGZero). Wwe should decrease the y value by 5 every time the screen is updated.   
```
def update():  
    frog.y -= 5
```    
11. Test the code
12. You will notice that the frog disappears off the screen never to be seen again. We need to reset the y value if we detect that the frog has gone off the screen.  
At the end of the update function, add these lines  
```
if frog.y < 0:  
    frog.y = HEIGHT + frog.height  
```
modify the initial positioning of the frog.  
```
    frog.pos(320,HEIGHT + frog.height )
```
13. Now test the code   










