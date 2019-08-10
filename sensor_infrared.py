# coding=utf-8
import RPi.GPIO as GPIO
import time


def isObstacle(GPIO_PIN):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_PIN, GPIO.IN)

    # 当有障碍物时，传感器输出低电平，所以检测低电平
    if GPIO.input(GPIO_PIN) == 0:
        GPIO.cleanup()
        return True
    else:
        GPIO.cleanup()
        return False


if __name__ == '__main__':
    pinInfra = 37
    while True:
        isHuman = isObstacle(pinInfra)
        if isHuman is True:
            print "there is something"
            time.sleep(2)
        else:
            print "there is nothing"
            time.sleep(2)
