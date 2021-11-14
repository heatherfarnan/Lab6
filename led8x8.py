# led8x8 class

import time
from shifter import Shifter

import multiprocessing

import random

a = multiprocessing.Array('i', 8)

class LED8x8():
  
  'Class for controlling an 8x8 LED display'

  a = [0b11111111, 0b11111111, 0b11111111, 0b111101111, 0b11111111, 0b11111111, 0b11111111, 0b11111111]
  i = 4

  #pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

    p = multiprocessing.Process(name='name', args=(a))

    p.daemon = True
    p.start()


  def display(self):
    for n in range(len(a)):
      self.shifter.shiftByte(a[n])
      self.shifter.shiftByte(1 << n)
      self.shifter.latch()
      time.sleep(.001)

  def randomwalk(self):
    r = random.randint(0,2)
    if r == 0:
      if LED8x8.i != 0:
        a[LED8x8.i-1] = a[LED8x8.i]
        print(a[LED8x8.i-1])
        a[LED8x8.i] = 0b1111111
        print(a[LED8x8.i-1])
        LED8x8.i -= 1
    if r == 1:
      pass
    if r == 2:
      if LED8x8.i != 7:
        a[LED8x8.i+1] = a[LED8x8.i]
        a[LED8x8.i] = 0b1111111
        LED8x8.i += 1
    c = random.randint(0,2)
    if c == 0:
      if a[LED8x8.i] < 256:
        a[LED8x8.i] << 1
        a[LED8x8.i] += 1
    if c == 1:
      pass
    if c == 2:
      if a[LED8x8.i] < 510:
        a[LED8x8.i] >> 1
        a[LED8x8.i] += 256
    time.sleep(.1)
    print(a[:])
    