import time
import board
import neopixel 
from messaging import Messsenger
import json

#LED Matrices Configuation
# Define the number of pixels in each LED matrix
NUM_PIXELS = 256
# Define the number of LED matrices connected
NUM_MATRICES = 6
# Move over by 1 column of pixels (16 pixels
SKIP_PIXELS  = 128
PIXELS_TO_LIGHT = 48
#move delay changes the speed of LED blocks
MOVE_DELAY = 0.2 #seconds
FPS = 90

# Initialize the LED Matrix
pixels = neopixel.NeoPixel (board.NEOPIXELo, NUM_PIXELS * NUM_MATRICES, brightness=1, autowrite=False)

# Define the current position of the pattern
current_pos = 0

# Define the color of the lit pixels
color = (0 , 0, 100)

# Flag to track the direction of the movement
move_forward = True

while True:
    #Check for incoming message from host PC
    #Replace this part with your own code for receiving messages
    incoming_message = "optomotor" #Replace with the actual message received
    
    if incoming_message == "optomotor"
        #Turn off all other pixels
    pixels.fill ((0, 0, 0))

    #Loop throuhgh the pixels in the pattern and light them up
    for i in range(current_pos, NUM_PIXELS * NUM_MATRICES, PIXELS_TO_LIGHT * 96)
        # Number of blocks per matrix
        if i + PIXELS_TO_LIGHT <= NUM_PIXELS * NUM_MATRICES:
            pixels[i:i+PIXELS_TO_LIGHT] = [color] * PIXELS_TO_LIGHT

    #Move the pattern to the right or left based on the direction
    if move_forward:
            current_pos += SKIP_PIXELS
    else:
            current_pos -= SKIP_PIXELS

    # Check if we've reached the end of the matrix
    if current_pos >= NUM_PIXELS * NUM_MATRICES or current_pos <= 0:
          #TOGGLE THE DIRECTION
        move_forward = not move_forward

    # Show the updated LED matrix
        pixels.show()

    # Wait for a short delay
        time.sleep(MOVE_DELAY)

#Add in option for stripe fixation
#Edit MOVE_DELAY to match angular velocity for most

