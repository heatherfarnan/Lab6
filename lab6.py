from led8x8 import LED8x8
#from shifter import Shifter

dataPin, latchPin, clockPin = 23, 24, 25

led = LED8x8(dataPin, latchPin, clockPin)
#shift = Shifter(dataPin, latchPin, clockPin)
#yuh

while True:
  led.display()
#  shift.latch()