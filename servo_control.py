import RPi.GPIO as GPIO
import time

# Set up GPIO
servo_pin = 18  # GPIO pin connected to the servo signal wire
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz frequency
pwm.start(0)

def set_angle(angle):
    duty_cycle = 2 + (angle / 18)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        angle = float(input("Enter angle (0-360): "))
        set_angle(angle)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    pwm.stop()
    GPIO.cleanup()
