import RPi.GPIO as GPIO
import time
import threading

# Ustawienia GPIO
GPIO.setmode(GPIO.BCM)
LED1_PIN = 17
LED2_PIN = 18

# Konfiguracja pinów jako wyjścia
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)

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
        time.sleep(0.3)  # 0.3 sekundy
        GPIO.output(LED2_PIN, GPIO.LOW)
        time.sleep(0.3)

# Uruchamianie wątków
try:
    thread1 = threading.Thread(target=blink_led1)
    thread2 = threading.Thread(target=blink_led2)
    thread1.daemon = True  # Dzięki temu wątki zakończą się przy zamykaniu programu
    thread2.daemon = True
    thread1.start()
    thread2.start()

    # Program działa w pętli, dopóki nie zostanie przerwany
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Zamykanie programu...")
    GPIO.cleanup()  # Czyszczenie ustawień GPIO
