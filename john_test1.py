import RPi.GPIO as GPIO
import time
# Configuration
LED_PIN = 21  # GPIO pin connected to the data pin of the WS2812B
NUM_LEDS = 300  # Number of LEDs in the strip
# Timing constants
T0H = 0.0000004  # 0.4us
T0L = 0.00000085  # 0.85us
T1H = 0.0000008  # 0.8us
T1L = 0.00000045  # 0.45us
RESET_TIME = 0.00005  # Reset signal low for 50us
# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
def send_bit(bit):
    if bit == 1:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(T1H)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(T1L)
    else:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(T0H)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(T0L)
def send_byte(byte):
    for i in range(8):
        send_bit((byte >> (7 - i)) & 1)
def send_color(g, r, b):
    send_byte(g)
    send_byte(r)
    send_byte(b)
def reset():
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(RESET_TIME)
# Main function
def set_led_color(r, g, b):
    send_color(g, r, b)
    reset()
if __name__ == "__main__":
    try:
        while True:
            # Red
            set_led_color(255, 0, 0)
            print("Setting LED RED")
            time.sleep(1)
            # Green
            set_led_color(0, 255, 0)
            print("Setting LED Green")
            time.sleep(1)
            # Blue
            set_led_color(0, 0, 255)
            print("Setting LED BLUE")
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()