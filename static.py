# Sense Hat STATIC
# By Ian Simpson @familysimpson

from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.clear()

print("STATIC")
password = input("Enter password to run program: ")
if password == "password":
	for y in range(0,8):
		for x in range(0,8):
			r = randint(0,255)
			g = randint(0,255)
			b = randint(0,255)
			sense.set_pixel(x,y,r,g,b)
	sleep(10)
	sense.clear()
	print("SUCCESS!")
else:
	print("FAILED!")
