from gpiozero import LED, Button, Buzzer
from time import sleep
from signal import pause
  
buzzer = Buzzer(2)  
button = Button(21)  
red = LED(17)
yellow = LED(11)
green = LED(26)


while True:            
            red.on()
            print("Stop")
            sleep(5)
            red.off()
            sleep(1)
            yellow.on()
            print("Get ready")
            sleep(3)
            yellow.off()
            sleep(1)
            green.on()
            print("Go go go")
            sleep(7)
            green.off()
            sleep(1)
            yellow.on()
            print("Get ready to stop")
            sleep(3)
            yellow.off()
            sleep(1)
            if button.is_pressed:
                buzzer.on()
                sleep(1)
                red.on()
                print("STOP")
                sleep(5)
                red.off()
                sleep(1)