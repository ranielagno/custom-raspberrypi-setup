import time, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def detectGas(pin):
    print "High Gas concentration detected!"
    return


GPIO.add_event_detect(18, GPIO.RISING)
GPIO.add_event_callback(18, detectGas)

GPIO.output(16, GPIO.HIGH)

try:
    while True:
        print "alive"
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
