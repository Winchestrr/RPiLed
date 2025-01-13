from time import sleep
from adafruit_pca9685 import PCA9685
import board
import busio

# Ustawienie I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Inicjalizacja PCA9685
pca = PCA9685(i2c)
pca.frequency = 1000  # Częstotliwość PWM

# Piny dla LED-ów
led1_pin = 0
#led2_pin = 1

# Funkcja do płynnego zapalania/gaszenia
def fade_led(pin, duration, steps):
    for i in range(steps):
        duty_cycle = int((i / steps) * 0xFFFF)
        pca.channels[pin].duty_cycle = duty_cycle
        sleep(duration / (2 * steps))
    #for i in range(steps, 0, -1):
     #   duty_cycle = int((i / steps) * 0xFFFF)
      #  pca.channels[pin].duty_cycle = duty_cycle
       # sleep(duration / (2 * steps))

try:
    while True:
        fade_led(led1_pin, duration=1, steps=50)  # Szybki fade in/out
        # fade_led(led2_pin, duration=2, steps=50)  # Wolniejszy fade in/out
finally:
    pca.deinit()
