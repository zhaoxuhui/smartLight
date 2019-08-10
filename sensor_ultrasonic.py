# coding=utf-8
import RPi.GPIO as GPIO
import time

Trig_Pin = 7
Echo_Pin = 11


def getDistance():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Trig_Pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Echo_Pin, GPIO.IN)
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 * 100 / 2


try:
    while True:
        dis = getDistance()
        print 'Distance:%0.2f cm' % dis
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
