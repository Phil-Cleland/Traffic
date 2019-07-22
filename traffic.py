from gpiozero import LED, Button
from time import sleep
from signal import pause
  
#buzzer = Buzzer(15)  
#button = Button()  
red = LED(17)
yellow = LED(11)
green = LED(26)


while True:  
           #print("Wait")
           
           red.on()
           print("Stop")
           sleep(7)
           red.off()
           sleep(1)
           yellow.on()
           print("Get ready")
           sleep(4)
           yellow.off()
           sleep(1)
           green.on()
           print("Go go go")
           sleep(8)
           green.off()
           sleep(1)
