from gpiozero import LED, Button
from time import sleep
from random import uniform
from os import _exit

    
def react():
    
    led = LED(4)
    
    right_button = Button(14)
    right_button.when_pressed = lambda button: pressed(button, led)
    
    left_button = Button(15)
    left_button.when_pressed = lambda button: pressed(button, led)
    
    led.on()
    
    number = uniform(2, 5)
    
    print(f"Number is {number}")
    
    sleep(number)
    
    led.off()
    
    pause()
    
    _exit(0)
    
def pressed(button, led):
    
    if button.pin.number == 14:
        
        print(left_name + " won the game")
    
    else:
        
        print(right_name + " won the game")
        
    led.off()
        
    _exit(0)
        
    
if __name__ == "__main__":
    
    left_name = input("Left player Name is: ")
    right_name = input("Right player Name is: ")
    
    react()