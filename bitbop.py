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
    while not Finish:
        inst = []
        for i in range(0,6):
            inst.append(random.randint(0,3))
 
        for i in inst:
            print(actions[i])
            if actions[i] == 'A':
                display.show("A",1000, wait=True,loop=False,clear=False)
                sleep(1000)
                if not button_a.was_pressed():
                    break
            if actions[i] == 'B':
                display.show("B",1000, wait=True,loop=False,clear=False)
                sleep(1000)
                if not button_b.was_pressed():
                    break
            if actions[i] == 'FA':
                FA = False
                display.show(Image.ARROW_N)
                start = running_time()
                sleep(1000)
                while (running_time() - start) < 1000:
                    if accelerometer.get_y() > 500:
                        FA = True
                if FA == False:
                    break
            if actions[i] == 'BA':
                BA = False
                display.show(Image.ARROW_S)
                start = running_time()
                sleep(1000)
                while (running_time() - start) < 1000:
                    if accelerometer.get_y() > -500:
                        BA = True
                if BA == False:
                    break
        Finish = True       
       
            
game = 0
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
display.scroll("Game Over", delay=175, wait=True, loop=True)