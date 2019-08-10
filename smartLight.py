# coding=utf-8
import RPi.GPIO as GPIO
import time
import sys


def ledLightRed(pinR, colorR=255, durTime=2):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinR, GPIO.OUT)
    pwmR = GPIO.PWM(pinR, 70)
    pwmR.start(0)
    R = 100 - int((colorR / 255.0) * 100)
    pwmR.ChangeDutyCycle(R)
    time.sleep(durTime)
    pwmR.stop()
    GPIO.cleanup()


def getDistance(trig_pin, echo_pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(echo_pin, GPIO.IN)
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(trig_pin, GPIO.LOW)
    while not GPIO.input(echo_pin):
        pass
    t1 = time.time()
    while GPIO.input(echo_pin):
        pass
    t2 = time.time()
    GPIO.cleanup()
    return (t2 - t1) * 340 * 100 / 2


def isHumanThereUltraSonic(trig_pin, echo_pin, lowTh, highTh):
    dist = getDistance(trig_pin=trig_pin, echo_pin=echo_pin)
    print "distance", dist, " cm"
    if lowTh <= dist <= highTh:
        return True
    else:
        return False


def isHumanThereInfrared(GPIO_PIN):
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

    # config parameters
    sleepTime = 1  # sample interval
    pinInfra = 37  # GPIO pin number(BOARD) of infrared obstacle sensor
    pinTrig = 7  # trig GPIO pin number(BOARD) of ultrasonic distance sensor
    pinR = 36  # GPIO pin number(BOARD) of LED
    pinEcho = 11  # echo GPIO pin number(BOARD) of ultrasonic distance sensor
    th_low = 10  # low distance threshold(unit:cm) for ultrasonic distance sensor
    th_high = 50  # high distance threshold(unit:cm) for ultrasonic distance sensor

    if len(sys.argv) == 1:
        print "======Use infrared sensor as default======"
        while True:
            isHuman = isHumanThereInfrared(pinInfra)
            if isHuman is True:
                print "there is a person"
                ledLightRed(pinR=pinR, durTime=sleepTime)
            else:
                print "there is no person"
                time.sleep(sleepTime)
    elif len(sys.argv) == 2:
        flag = sys.argv[1]
        if flag == "infra" or flag == "Infra" or flag == "INFRA":
            print "======Use infrared sensor======"
            while True:
                isHuman = isHumanThereInfrared(pinInfra)
                if isHuman is True:
                    print "there is a person"
                    ledLightRed(pinR=pinR, durTime=sleepTime)
                else:
                    print "there is no person"
                    time.sleep(sleepTime)
        elif flag == "ultra" or flag == "Ultra" or flag == "ULTRA":
            print "======Use ultrasonic sensor======"
            while True:
                isHuman = isHumanThereUltraSonic(pinTrig, pinEcho, th_low, th_high)
                if isHuman is True:
                    print "there is a person"
                    ledLightRed(pinR=pinR, durTime=sleepTime)
                else:
                    print "there is no person"
                    time.sleep(sleepTime)
        else:
            print "check input parameters."
    else:
        print "check input parameters."
