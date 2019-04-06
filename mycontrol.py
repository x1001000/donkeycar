import RPi.GPIO as GPIO
L298N_In1=35
L298N_In2=37
L298N_In3=36
L298N_In4=38
L298N_En12=32
L298N_En34=33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(L298N_In1, GPIO.OUT)
GPIO.setup(L298N_In2, GPIO.OUT)
GPIO.setup(L298N_In3, GPIO.OUT)
GPIO.setup(L298N_In4, GPIO.OUT)
GPIO.setup(L298N_En12, GPIO.OUT)
GPIO.setup(L298N_En34, GPIO.OUT)
GPIO.output(L298N_In1, GPIO.HIGH)
GPIO.output(L298N_In2, GPIO.LOW)
GPIO.output(L298N_In3, GPIO.HIGH)
GPIO.output(L298N_In4, GPIO.LOW)
en12 = GPIO.PWM(L298N_En12, 123)
en34 = GPIO.PWM(L298N_En34, 123)
en12.start(0)
en34.start(0)
class control:
    def __init__(self):
        pass
    def run(self, angle, throttle):
        #print('throttle:', round(throttle, 2))
        #print('Moving!' if throttle > 0.5 else 'Stopped...')
        if throttle > 0:
            dc12 = throttle * 90
            dc34 = throttle * 100
            if angle > 0:
                dc34 *= (1 - angle)
            elif angle < 0:
                dc12 *= (1 + angle)
            en12.ChangeDutyCycle(dc12)
            en34.ChangeDutyCycle(dc34)
        else:
            en12.ChangeDutyCycle(0)
            en34.ChangeDutyCycle(0)
    def shutdown(self):
        #self.run(0, 0)
        en12.stop()
        en34.stop()
        GPIO.cleanup()
