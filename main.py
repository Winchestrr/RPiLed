import RPi.GPIO as GPIO
import time
import threading

# Ustawienia GPIO
GPIO.setmode(GPIO.BCM)
LED1_PIN = 17
LED2_PIN = 18
LED3_PIN = 22
LED4_PIN = 23
LED5_PIN = 24

# Konfiguracja pinów jako wyjścia
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.setup(LED3_PIN, GPIO.OUT)
GPIO.setup(LED4_PIN, GPIO.OUT)
GPIO.setup(LED5_PIN, GPIO.OUT)

# Funkcja do mrugania LED1
def blink_led1():
    while True:
        GPIO.output(LED1_PIN, GPIO.HIGH)
        time.sleep(1)  # 1 sekunda
        GPIO.output(LED1_PIN, GPIO.LOW)
        time.sleep(1)

# Funkcja do mrugania LED2
def blink_led2():
    while True:
        GPIO.output(LED2_PIN, GPIO.HIGH)
        time.sleep(0.05)  # 0.3 sekundy
        GPIO.output(LED2_PIN, GPIO.LOW)
        time.sleep(0.05)

def wave():
    wait_time = 0.1
    while True:
        GPIO.output(LED1_PIN, GPIO.HIGH)
        time.sleep(wait_time)
        GPIO.output(LED2_PIN, GPIO.HIGH)
        time.sleep(wait_time)
        GPIO.output(LED3_PIN, GPIO.HIGH)
        time.sleep(wait_time)
        GPIO.output(LED1_PIN, GPIO.LOW)
        GPIO.output(LED4_PIN, GPIO.HIGH)
        time.sleep(wait_time)
        GPIO.output(LED2_PIN, GPIO.LOW)
        GPIO.output(LED5_PIN, GPIO.HIGH)
        time.sleep(wait_time)
        GPIO.output(LED3_PIN, GPIO.LOW)
        time.sleep(wait_time)
        GPIO.output(LED4_PIN, GPIO.LOW)
        time.sleep(wait_time)
        GPIO.output(LED5_PIN, GPIO.LOW)
        time.sleep(wait_time)

def turn_on_off():
    GPIO.output(LED5_PIN, GPIO.HIGH)
    time.sleep(0.08)
    GPIO.output(LED5_PIN, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(LED5_PIN, GPIO.HIGH)
    time.sleep(0.03)
    GPIO.output(LED5_PIN, GPIO.LOW)
    time.sleep(0.03)
    GPIO.output(LED5_PIN, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(LED5_PIN, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(LED5_PIN, GPIO.HIGH)

    GPIO.output(LED4_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(LED4_PIN, GPIO.LOW)
    time.sleep(0.03)
    GPIO.output(LED4_PIN, GPIO.HIGH)
    time.sleep(0.037)
    GPIO.output(LED4_PIN, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(LED4_PIN, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED4_PIN, GPIO.LOW)
    time.sleep(0.03)
    GPIO.output(LED4_PIN, GPIO.HIGH)

    GPIO.output(LED3_PIN, GPIO.HIGH)
    time.sleep(0.15)
    GPIO.output(LED3_PIN, GPIO.LOW)
    time.sleep(0.04)
    GPIO.output(LED3_PIN, GPIO.HIGH)
    time.sleep(0.02)
    GPIO.output(LED3_PIN, GPIO.LOW)
    time.sleep(0.04)
    GPIO.output(LED3_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED3_PIN, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(LED3_PIN, GPIO.HIGH)

    time.sleep(2)
    GPIO.cleanup()

try:
    # GPIO.cleanup()
    # wave()
    turn_on_off()


except KeyboardInterrupt:
    GPIO.cleanup()
