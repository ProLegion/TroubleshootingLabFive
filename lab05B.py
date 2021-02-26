import RPi.GPIO as GPIO             #GPIO Libraries
import gpiozero                     #More GPIO Libraries, these have better documentation than PRi.GPIO so I prefer it
from time import sleep

#Initalize LED using gpiozero library
led = gpiozero.LED(21)

#initalize input
GPIO.setmode(GPIO.BCM)
GPIO.setup(
    18,                             #Using pin 12(GPIO 18)
    GPIO.IN,                        #Make pin 12 input
    pull_up_down = GPIO.PUD_UP      #Enable Internal PullUp resistors
)


#Instead of outputing for every detcted low input, which works fine when using a button,
#it doesn't work so we with swtiches. My soloution to this was to Check the input against 
#it's previous state, and only activates the if/else tree if a change is detected. I also
#made it so the program turns an led on or off depending on the state of the switch.


inputState = GPIO.input(18)         #Give inputState an inital Value
if(inputState == False):    #If changed, determine what action needs to be taken
        led.on()
        print("Input is Low, switch is closed\n")
else:
    led.off()
    print("Input is High, switch is open\n")     

while(True):                        #loop always                    
    lastState = inputState          #Pass off the current state to our last state
    inputState = GPIO.input(18)     #Refresh current state value
    if(inputState != lastState):    #Check for change between states
        if(inputState == False):    #If changed, determine what action needs to be taken
            led.on()
            print("Change Detected...")
            print("Input is Low, switch is closed\n")
        else:
            led.off()
            print("Change Detected...")
            print("Input is High, switch is open\n")
    sleep(0.1)                      #trigger small delay
           