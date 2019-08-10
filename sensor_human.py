# coding=utf-8
import RPi.GPIO as GPIO
import time

time_out = 2
human = 35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(human, GPIO.IN)

try:
    while True:
        if (GPIO.input(human) == True):
            print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " Someone is here!"
        else:
            print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " No one!"
        time.sleep(time_out)
except:
    pass
GPIO.cleanup()
