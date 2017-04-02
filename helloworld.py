# Sense Hat HELLOWORLD
# By Ian Simpson @familysimpson

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

print("HELLOWORLD")
yourname = input("Enter your name: ")
message = "Hello from "+ yourname
sense.show_message(message, text_colour=(255,0,0))
