import time
import board
import neopixel

# LED strip configuration:
LED_COUNT = 300        # Number of LED pixels.
LED_PIN = board.D18    # GPIO pin connected to the pixels (must support PWM).
LED_BRIGHTNESS = 0.2   # Set to 20% brightness (0.2)

# Create NeoPixel object with appropriate configuration.
strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False)

def set_all_white(strip):
    """Set all LEDs to white at 20% brightness."""
    strip.fill((255, 255, 255))
    strip.show()

if __name__ == '__main__':
    try:
        while True:
            set_all_white(strip)
            time.sleep(1)  # Keep the LEDs on
    except KeyboardInterrupt:
        # Clear the strip on exit
        strip.fill((0, 0, 0))
        strip.show()


# This is my cool comment