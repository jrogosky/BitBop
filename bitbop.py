#Game play
#Jumping Game - Random number or set to jump so many times
#   - read the Z accelerometer for a difference of ???
#Stand Still for x seconds
#Compass game - follow x numbr of directions
#button press (DDR) - Point left, point right randomly
# Reaction time - 3 correct button presses
from microbit import *
import random

def instructions(Message):
    while True:
        display.scroll(Message, delay=100, wait=True, loop=False)
        if button_a.was_pressed():
            break
    return
    
def GoodJob():
    display.scroll("GOOD JOB!", delay=175, wait=True, loop=False)
    return

#creates the jumping game
def jumpGame():
    instructions("JUMP 5 TIMES, PRESS A WHEN READY")
    jump_counter = 0
    while jump_counter < 4:
        display.clear()
        cng_z = accelerometer.get_z()
        if cng_z > 100:
            jump_counter+=1
            display.show(str(5-jump_counter),1000, wait=True,loop=False,clear=False)
            cng_z = 0
            sleep(1500)
        else:
            display.show(str(5-jump_counter),1000, wait=True,loop=False,clear=False)
        
def standStill():
    instructions("HOLD ME FLAT FOR 5 SECONDS, PRESS A WHEN READY")
    start = running_time()
    display.show(Image.HAPPY)
    while True:
        display.show(Image.HAPPY)
        cng_z = accelerometer.get_z()
        cng_x = accelerometer.get_x()
        cng_y = accelerometer.get_y()
        if (cng_z > 75 or cng_y > 75 or cng_x > 75):
            print("x:" + str(cng_x) + " y:" + str(cng_y) + " z:"+ str(cng_z))
            display.show(Image.SAD)
            sleep(2000)
            start = running_time()
        if (running_time() - start) > 5000:
            break
            
def react():
    actions=['A','FA','BA','B']
    instructions("FOLLOW THE INSTRUCTIONS, PRESS A WHEN READY")
    Finish = False
    inst = []
    for i in range(0,6):
        inst.append(random.randint(0,3))
 
    for i in inst:
        print(actions[i])
        if actions[i] == 'A':
            display.show("A",1000, wait=False,loop=False,clear=False)
            while True:
                if button_a.was_pressed():
                    break
        if actions[i] == 'B':
            display.show("B",1000, wait=True,loop=False,clear=False)
            while True:
                if button_b.was_pressed():
                    break
        if actions[i] == 'FA':
            display.show(Image.ARROW_N)
            while (accelerometer.get_y() < 500):
                sleep(1)
        if actions[i] == 'BA':
            display.show(Image.ARROW_S)
            while accelerometer.get_y() > -500:
                sleep(1)

#point the microbit in the listed direction   
def CompassPoint():
    directions=["N","S","E","W"]
    instructions("TURN THE MICROBIT TOWARDS THE DIRECTION SHOWN, PRESS A WHEN READY")
    Finish = False
    while not Finish:
        inst = []
        for i in range(0,6):
            inst.append(random.randint(0,3))
        for i in inst:
            if (directions[i] == "N"):
                while (not compass.heading() == 0):
                    print(str(compass.heading()))
                    display.show("N",100, wait=False,loop=False,clear=False)
            if (directions[i] == "E"):
                while (not compass.heading() == 90):
                    print(str(compass.heading()))
                    display.show("E",100, wait=False,loop=False,clear=False)
            if (directions[i] == "S"):
                while (not compass.heading() == 180):
                    print(str(compass.heading()))
                    display.show("S",100, wait=False,loop=False,clear=False)
            if (directions[i] == "W"):
                while (not compass.heading() == 270):
                    print(str(compass.heading()))
                    display.show("W",100, wait=False,loop=False,clear=False)
#Starts at random number, press button A to go up, B to go down until you find the temp
def findTemp():
    start = random.randint(20,85)
    currTemp = round(temperature() * 1.8 + 32)
    currTempStr = str(currTemp)
    print(str(currTemp) + "," + str(start))
    
    display.scroll("Curr Temp is: " + currTempStr, delay=100, wait=True, loop=False)
    
    
#Tracks what game is the current one.           
game = 0
#scrolls text
instructions("ARE YOU READY TO PLAY, PRESS A")
while game < 6:  
    if game == 0:
        jumpGame()
        GoodJob()
        game = 1
    if game == 1:
       standStill()
       GoodJob()
       game = 2
    if game == 2:
       react()
       GoodJob()
       game = 6
#Compass is too unreliable, will need to replace
    if game == 3:
       CompassPoint()
       GoodJob()
       game = 6   
display.scroll("Game Over", delay=175, wait=True, loop=True)