import time
import board
import neopixel

# Configuration
LED_PIN = board.D21  # GPIO pin connected to the data pin of the WS2812B
NUM_LEDS = 300  # Number of LEDs in the strip

# Create NeoPixel object with appropriate configuration.
pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=0.2, auto_write=False)

def set_color(color):
    pixels.fill(color)
    pixels.show()

try:
    while True:
        set_color((51, 51, 51))  # White at 20% brightness
        print("Setting LED WHITE at 20% brightness")
        time.sleep(1)
except KeyboardInterrupt:
    set_color((0, 0, 0))  # Turn off all LEDs
    print("LEDs turned off")
