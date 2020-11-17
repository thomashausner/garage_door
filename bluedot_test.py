#!/usr/bin/env python3

from bluedot import BlueDot
from gpiozero import LED
from signal import pause

bd = BlueDot()
led = LED(17)

bd.when_pressed = led.on
bd.when_released = led.off

pause()
