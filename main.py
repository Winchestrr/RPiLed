import RPi.GPIO as GPIO
import time

# Ustawienie numeracji pinów GPIO na fizyczne numery pinów
GPIO.setmode(GPIO.BOARD)

# Definicja pinów, do których podłączone są diody
LED1 = 17
LED2 = 18

# Ustawienie pinów jako wyjścia
GPIO.setup(LED1, GPIO.BCM)
GPIO.setup(LED2, GPIO.BCM)

# Funkcja do mrugania diodą
def mrugaj(pin, czas):
    while True:
        GPIO.output(pin, GPIO.HIGH)  # Zapal dioda
        time.sleep(czas)
        GPIO.output(pin, GPIO.LOW)   # Zgaś dioda
        time.sleep(czas)

# Utworzenie dwóch wątków do mrugania diodami
try:
    import threading
    thread1 = threading.Thread(target=mrugaj, args=(LED1, 1))
    thread2 = threading.Thread(target=mrugaj, args=(LED2, 0.3))
    thread1.start()
    thread2.start()

    while True:
        pass

except KeyboardInterrupt:
    # Czyszczenie stanu pinów GPIO przy przerwaniu
    GPIO.cleanup()