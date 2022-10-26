from sense_hat import SenseHat

def greet_message(message):
    
    sense = SenseHat()
    
    """

    """
    # sense.show_message("Hi, Li Ze Xiao", text_colour = (255 ,255, 0), back_colour = (0, 0, 255), scroll_speed = (0.05))
    
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    
    while True:
    
        sense.show_message(message, text_colour = yellow, back_colour = blue, scroll_speed = (0.1))

def greet_letter(letter):
    
    sense = SenseHat()
    red = (255, 0, 0)
    
    sense.show_letter(letter, text_colour = red)
    
if __name__ == "__main__":
    
    greet_message("Hi, Li Ze Xiao")
    greet_letter('Z')