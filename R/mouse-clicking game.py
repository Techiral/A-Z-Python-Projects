from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=1366, height=768, background="black")

def setInitialValues():
    global xRocket, yRocket, ySpeed, flame, startMessage, deathMessage, randomInsults, gameRunning

    xRocket = 400
    yRocket = 100
    ySpeed = 0
    flame = 0
    deathMessage = 0
    randomInsults = ["dummy", "moron", "fool", "klutz", "dope", "noob", "goof ball", "wart nosed buffoon"]
    startMessage = screen.create_text(100,100,text="Click to fire the rocket's thruster", font = "Times 18",fill="red", anchor=W)
    gameRunning = True

 
def drawRocket():
    global rocketBase, rocketNose

    rocketBase = screen.create_rectangle(xRocket, yRocket, xRocket+50, yRocket+100, fill="blue", outline="blue" )
    rocketNose = screen.create_polygon( xRocket, yRocket, xRocket+25, yRocket-25, xRocket+50, yRocket, fill="yellow", outline="DodgerBlue" ) 


#Every time the player clicks the mouse, this procedure gets called. The procedure increases the upward speed of the rocket.
def mouseClickHandler( event ):
    global ySpeed, flame
    
    if gameRunning == True:
        ySpeed = ySpeed - 5 #increase the rocket's upward speed
        flame = screen.create_polygon( xRocket, yRocket+100, xRocket+50, yRocket+100, xRocket+25, yRocket+210, fill="red")

    
def mouseReleaseHandler( event ):
    global flame
    
    screen.delete(flame)
    

def endGame():
    global startMessage, deathMessage, gameRunning

    gameRunning = False
    
    screen.delete(startMessage)
    
    insult = choice(randomInsults)
    deathMessage = screen.create_text(200, 400, text="You crashed the ship. Try again, " + insult + ".", font = "Times 24", anchor=W, fill="red" )

    screen.update()
    sleep(2)
    screen.delete(deathMessage)
    

def startRocketProgram():
    global yRocket, ySpeed, flame, startMessage
       
    setInitialValues()

    while yRocket < 600: #Keep the game running until the rocket's y-level falls below 600
        
        yRocket = yRocket + ySpeed  #Update the rocket's vertical position using its current speed
        ySpeed = ySpeed + 1         #Gravity is constantly increasing the rocket's downward speed
        drawRocket()
        screen.update()
        sleep(0.05)
        screen.delete( rocketBase, rocketNose, flame )

    endGame()

    startRocketProgram() #restart



root.after(500, startRocketProgram) #start the game 500 milliseconds after pushing F5 by calling the procedure named startRocketProgram().
screen.bind("<Button-1>", mouseClickHandler) #makes the procedure named mouseClickHandler() get called every time the user clicks the left mouse button.
screen.bind("<ButtonRelease-1>", mouseReleaseHandler) 
screen.pack()
screen.focus_set()
root.mainloop()
