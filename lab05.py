#Instrumentation & Troubleshooting Lab 5
#Using GPIO pins on the Raspberry Pi
#Owen Cantor

import RPi.GPIO as GPIO         #Library that contains useful functions for controlling the Pi
import time                     #Contains time functions

# #Setup GPIO pin
# GPIO.setmode(GPIO.BCM)          #Set RPi to reference GPIO Number instead of Pin #
# GPIO.setwarnings(False)         #Pi might give warnings if pins are already in use, ignore the warnings
# GPIO.setup(18,GPIO.OUT)         #Set GPIO 18 to an GPIO output

# #Modification to keep the LED blinking
# while(True):
#     #Turn LED ON
#     print("LED On...")
#     GPIO.output(18,GPIO.HIGH)   #Set GPIO 18 High to turn on LED
#     time.sleep(0.25)            #Pause for 1/4 second

#     #Turn LED OFF
#     print("LED Off...")
#     GPIO.output(18,GPIO.LOW)    #Sets GPIO 18 low to turn off LED
#     time.sleep(0.25)            #Wait for anothercler 1/4 second

GPIO.setmode(GPIO.BOARD)
GPIO.setup(
    12,                         #Using pin 12(GPIO 18)
    GPIO.IN,                    #Make pin 12 input
    pull_up_down = GPIO.PUD_UP  #Enable Internal PullUp resistors
)

while(True):
    input_state=GPIO.input(12)  #Get the state of input, input is active low
    if input_state == False:    #When pin 12 drops low(input_state == false), button is presssed
        print("Button Pressed") #Print message to terminal
        time.sleep(0.25)        #Quick delay
