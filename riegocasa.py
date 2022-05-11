  GNU nano 2.7.4                 File: riegorancho.py                  Modified  

#!/usr/bin/python
import RPi.GPIO as gp

import time


gp.setmode(gp.BOARD)
gp.setwarnings(False)
macetas =  12
jardinera = 36
pasto = 18
atras = 32
gp.setup(macetas, gp.OUT)
gp.setup(jardinera, gp.OUT)
gp.setup(pasto, gp.OUT)
gp.setup(atras, gp.OUT)

time.sleep(.2)
gp.output(macetas, 0)
gp.output(jardinera, 0)
gp.output(pasto, 1)
time.sleep(60)
gp.output(atras, 0)
gp.output(jardinera, 1)
time.sleep(60)
gp.output(pasto, 0)
time.sleep(60)
gp.output(macetas, 1)
time.sleep(60)
gp.output(atras, 1)
quit()
