import time, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def detectMediumGasConcentration(pin):
    print('Medium Gas concentration detected!')
    return

def detectHighGasConcentration(pin):
    print('High Gas concentration detected!)
    return

GPIO.add_event_detect(14, GPIO.RISING)
GPIO.add_event_callback(14, detectMediumGasConcentration)

GPIO.add_event_detect(15, GPIO.RISING)
GPIO.add_event_callback(15, detectHighGasConcentration)

try:
    while True:
        print('alive')
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
