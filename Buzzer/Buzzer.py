from gpiozero import Buzzer
from time import sleep

def buzz():
    
    buzzer = Buzzer(21)
    
    while True:
        
        buzzer.on()
        sleep(1)
        
        buzzer.off()
        sleep(1)
        
if __name__ == "__main__":
    
    buzz()