from machine import Pin
import neopixel
import time
pin = Pin(16, Pin.OUT)
np = neopixel.NeoPixel(pin,1)

#brightness :0-255
brightness=10                                
colors=[[brightness,0,0],                    #red
        [0,brightness,0],                    #green
        [0,0,brightness],                    #blue
        [brightness,brightness,brightness],  #white
        [0,0,0]]                             #close
    
while True:
    for i in range(0,5):
        np[0]=colors[i]
        np.write()
        time.sleep_ms(500)
    time.sleep_ms(500)
    
    
