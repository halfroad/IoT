import time

from RPi import GPIO as GPIO

def setup():
    
    gpio = 20
    timeout = 5
    
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio, GPIO.IN)
    
    return gpio, timeout

def detect(gpio, timeout):
    
    try:
    
        while True:
            
            if GPIO.input(gpio):
                print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time())) + " - Someone presents")
            else:
                print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time())) + " - None presents")
                
            time.sleep(timeout)
            
    except KeyboardInterrupt:
        
        pass
    
    RPi.GPIO.cleanup()
    
def main():
    
    gpio, timeout = setup()
    detect(gpio, timeout)
    
if __name__ == "__main__":
    
    main()