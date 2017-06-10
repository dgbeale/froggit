# froggit step 02

# This steps will get the frog moving across the screen

1. Within the froggit folder, create a folder called step-02
2. Copy main.py from step-01
3. If not already - Start Python IDLE
4. If not already - Start a Windows Command Line session - position IDLE and Command next to each other
5. Within the command line session, navigate to the step-01 folder (cd  _HOME_ froggit/step-02)
6. Download the images folder from this githib directory to your step-02 folder (thanks to www.gameartguppy.com)
7. Commet the code to show different areas :  
''' Declarations '''    underneath the two variables
''' Game Loop '''   A few lines underneath

8. Declare variable for the frog within declararions section - this is a special type called Actor. We will passed it the name of the frog image we require.  
    frog = Actor("frog1") . 
9. Set the initial position of the frog udnerneath.   
    frog.pos(320,100)
10. Draw the frog, last line within the draw function.  
    frog.draw() 
11. Test the code
12. No we need to animate the frog, create a new function called update (this is called by PGZero). Now we should decrease the Y value by 5 every time the screen is updated.   
def update():  
    frog.y -= 5
13. Test the code
14. You will notice that the forg disappear off the screen never to be seen again. We need to reset the y value if we detect that the frog has gone off the screen.  
At the end of the update function, add these lines  
if frog.y < 0:  
    frog.y = HEIGHT + frog.height  

modify the initial positioning of the frog.  
    frog.pos(320,HEIGHT + frog.height )

15. Now test the code   










