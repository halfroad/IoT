from sense_hat import SenseHat
from time import sleep

def light_up():
    
    sense = SenseHat()
    
    sense.clear()
    
    red = (255, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    
    light1 = red
    light2 = green
    
    COUNTER = 6
    first = True
    relight = True
    count_down = COUNTER
    
    while(count_down >= 0):
        
        if not first and count_down == 1:
            
            light1 = (red if light1 == green else green)
            light2 = (red if light1 == green else green)
            
            relight = True
            
        else:
            
            relight = False
        
        if first or relight:
            
            # Light 1.0
            sense.set_pixel(0, 3, light1)
            # sense.set_pixel(1, 3, light1)
            sense.set_pixel(0, 4, light1)
            # sense.set_pixel(1, 4, light1)
                
            # Light 1.1
            # sense.set_pixel(6, 3, light1)
            sense.set_pixel(7, 3, light1)
            # sense.set_pixel(6, 4, light1)
            sense.set_pixel(7, 4, light1)
                
            # Light 2.0
            sense.set_pixel(3, 0, light2)
            sense.set_pixel(4, 0, light2)
            # sense.set_pixel(3, 1, light2)
            # sense.set_pixel(4, 1, light2)
                
            # Light 2.1
            # sense.set_pixel(3, 6, light2)
            # sense.set_pixel(4, 6, light2)
            sense.set_pixel(3, 7, light2)
            sense.set_pixel(4, 7, light2)
            
            first = False
        
        # sense.show_letter(f"{count_down}")
        show_number(sense, count_down)
        
        count_down -= 1
        
        sleep(1)
        
        if count_down == 0:
            
            count_down = COUNTER
        
def show_number(sense: SenseHat, i):
    
    sense.clear()
    
    blue = (0, 0, 255)
    
    if i == 1:
        
        sense.set_pixel(3, 2, blue)
        sense.set_pixel(4, 2, blue)
        sense.set_pixel(4, 3, blue)
        sense.set_pixel(4, 4, blue)
        sense.set_pixel(4, 5, blue)
        sense.set_pixel(4, 6, blue)
        sense.set_pixel(3, 6, blue)
        sense.set_pixel(4, 6, blue)
        sense.set_pixel(5, 6, blue)
        
    elif i == 2:
        
        sense.set_pixel(2, 2, blue)
        sense.set_pixel(3, 2, blue)
        sense.set_pixel(4, 2, blue)
        sense.set_pixel(5, 2, blue)
        
        sense.set_pixel(5, 3, blue)
        sense.set_pixel(5, 4, blue)
        
        sense.set_pixel(4, 4, blue)
        sense.set_pixel(3, 4, blue)
        sense.set_pixel(2, 4, blue)
        
        sense.set_pixel(2, 5, blue)
        sense.set_pixel(2, 6, blue)
        sense.set_pixel(3, 6, blue)
        sense.set_pixel(4, 6, blue)
        sense.set_pixel(5, 6, blue)
        
    elif i == 3:
        
        sense.set_pixel(2, 2, blue)
        sense.set_pixel(3, 2, blue)
        sense.set_pixel(4, 2, blue)
        sense.set_pixel(5, 2, blue)
        
        sense.set_pixel(5, 3, blue)
        sense.set_pixel(5, 4, blue)
        
        sense.set_pixel(4, 4, blue)
        sense.set_pixel(3, 4, blue)
        sense.set_pixel(2, 4, blue)
        
        sense.set_pixel(5, 5, blue)
        sense.set_pixel(5, 6, blue)
        
        sense.set_pixel(5, 6, blue)
        sense.set_pixel(4, 6, blue)
        sense.set_pixel(3, 6, blue)
        sense.set_pixel(2, 6, blue)
        
    elif i == 4:
        
        sense.set_pixel(5, 2, blue)
        sense.set_pixel(4, 3, blue)
        sense.set_pixel(3, 4, blue)
        sense.set_pixel(2, 5, blue)
        
        sense.set_pixel(3, 5, blue)
        sense.set_pixel(4, 5, blue)
        sense.set_pixel(5, 5, blue)
        sense.set_pixel(6, 5, blue)
        
        sense.set_pixel(5, 2, blue)
        sense.set_pixel(5, 3, blue)
        sense.set_pixel(5, 4, blue)
        sense.set_pixel(5, 5, blue)
        sense.set_pixel(5, 6, blue)
        
    
if __name__ == "__main__":
    
    light_up()
    show_number(1)