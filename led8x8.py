# led8x8 class

import time
from shifter import Shifter

class LED8x8():
  
  'Class for controlling an 8x8 LED display'

  pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

  def display(self):
    for n in range(len(LED8x8.pattern)):
      self.shifter.shiftByte(LED8x8.pattern[n])
      self.shifter.shiftByte(1 << n)
      self.shifter.ping(self.latchPin)
      time.sleep(.001)
