import RPi.GPIO as GPIO

L298N_EnA = 32
L298N_EnB = 33
L298N_In1 = 35
L298N_In2 = 36
L298N_In3 = 37
L298N_In4 = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(L298N_In1, GPIO.OUT)
GPIO.setup(L298N_In2, GPIO.OUT)
GPIO.setup(L298N_In3, GPIO.OUT)
GPIO.setup(L298N_In4, GPIO.OUT)
GPIO.setup(L298N_EnA, GPIO.OUT)
GPIO.setup(L298N_EnB, GPIO.OUT)
GPIO.output(L298N_In1, GPIO.HIGH)
GPIO.output(L298N_In2, GPIO.LOW)
GPIO.output(L298N_In3, GPIO.HIGH)
GPIO.output(L298N_In4, GPIO.LOW)
enL = GPIO.PWM(L298N_EnA, 1000)
enR = GPIO.PWM(L298N_EnB, 1000)
enL.start(0)
enR.start(0)

class control:
    def __init__(self):
        pass
    def run(self, angle, throttle):
        if throttle > 0:
            dcL = throttle * 100
            dcR = throttle * 100
            if angle < 0:
                dcL *= (1 + angle)
            else:
                dcR *= (1 - angle)
            print(dcL, dcR)
            enL.ChangeDutyCycle(dcL)
            enR.ChangeDutyCycle(dcR)
        else:
            enL.ChangeDutyCycle(0)
            enR.ChangeDutyCycle(0)
    def shutdown(self):
        #self.run(0, 0)
        enL.stop()
        enR.stop()
        GPIO.cleanup()
