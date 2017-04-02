# Sense Hat SKULL
# By Ian Simpson @familysimpson

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
sense.clear()

B = (0,0,0)
W = (255,255,255)

skull_pixels = [
    B, B, W, W, W, W, W, B,
    B, W, W, W, W, W, W, W,
    B, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    W, B, B, W, B, B, W, W,
    W, W, B, W, W, B, W, W,
    B, W, W, B, W, W, B, B,
    B, B, W, W, W, W, B, B
]

sense.set_pixels(skull_pixels)

print("SKULL")
sleep(2)
sense.clear()
