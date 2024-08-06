import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 300        # Number of LED pixels.
LED_PIN = 18           # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800kHz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 51    # Set to 20% brightness (255 * 0.2 = 51)
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0

# Create PixelStrip object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def set_color(strip, color):
    """Set all pixels in the strip to the given color."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

# Main program logic:
if __name__ == '__main__':
    try:
        while True:
            # Set strip to white at 20% brightness
            set_color(strip, Color(51, 51, 51))
            time.sleep(10)  # Keep the LEDs on for 10 seconds
    except KeyboardInterrupt:
        # Clear the strip on exit
        set_color(strip, Color(0, 0, 0))
