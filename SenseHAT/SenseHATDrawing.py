from sense_hat import SenseHat
from time import sleep

def draw():
    
    sense = SenseHat()
    
    # sense.clear(255, 255, 255)
    # sense.clear(0, 255, 0)
    sense.clear()
    
    """

    sense.set_pixel(0, 2, (0, 0, 255))
    sense.set_pixel(7, 4, (255, 0, 0))
    
    """
    
    sense.set_pixel(2, 2, (0, 0, 255))
    sense.set_pixel(4, 2, (0, 0, 255))
    sense.set_pixel(3, 4, (100, 0, 0))
    sense.set_pixel(1, 5, (255, 0, 0))
    sense.set_pixel(2, 6, (255, 0, 0))
    sense.set_pixel(3, 6, (255, 0, 0))
    sense.set_pixel(4, 6, (255, 0, 0))
    sense.set_pixel(5, 5, (255, 0, 0))
    
def draw_pixels():
    
    sense = SenseHat()
    
    # sense.clear(255, 255, 255)
    # sense.clear(0, 255, 0)
    sense.clear()
     
    green = (0, 255, 0)
    black = (0, 0, 0)
     
    creeper_pixels = [
         
        green, green, green, green, green, green, green, green,
        green, green, green, green, green, green, green, green,
        green, black, black, green, green, black, black, green,
        green, black, black, green, green, black, black, green,
        green, green, green, black, black, green, green, green,
        green, green, black, black, black, black, green, green,
        green, green, black, black, black, black, green, green,
        green, green, black, green, green, black, green, green,
         
        ]
     
    sense.set_pixels(creeper_pixels)
     
def rotate():
    
    sense = SenseHat()
    
    # sense.clear(255, 255, 255)
    # sense.clear(0, 255, 0)
    sense.clear()
     
    green = (0, 255, 0)
    black = (0, 0, 0)
     
    creeper_pixels = [
         
        green, green, green, green, green, green, green, green,
        green, green, green, green, green, green, green, green,
        green, green, green, green, green, black, black, green,
        green, green, green, green, green, black, black, green,
        green, green, green, black, black, green, green, green,
        green, green, black, black, black, black, green, green,
        green, green, black, black, black, black, green, green,
        green, green, black, green, green, black, green, green,
         
        ]
     
    sense.set_pixels(creeper_pixels)
    
    while True:
        
        sleep(1)
            
        sense.flip_h()
    
if __name__ =="__main__":
    
    draw()
    draw_pixels()
    rotate()