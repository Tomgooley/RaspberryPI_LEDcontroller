import spidev
import time

# Configuration
LED_PIN = 0  # SPI channel (0 or 1)
NUM_LEDS = 300  # Number of LEDs in the strip

# Timing constants (in microseconds)
T0H = 0.4  # 0.4us
T0L = 0.85  # 0.85us
T1H = 0.8  # 0.8us
T1L = 0.45  # 0.45us
RESET_TIME = 50  # Reset signal low for 50us

# Setup SPI
spi = spidev.SpiDev()
spi.open(0, LED_PIN)
spi.max_speed_hz = 8000000  # 8MHz

def send_bit(bit):
    if bit == 1:
        spi.xfer2([0b11100000])
    else:
        spi.xfer2([0b10000000])

def send_byte(byte):
    for i in range(8):
        send_bit((byte >> (7 - i)) & 1)

def send_color(g, r, b):
    send_byte(g)
    send_byte(r)
    send_byte(b)

def reset():
    time.sleep(RESET_TIME / 1000000.0)

# Main function
def set_led_color(r, g, b):
    for _ in range(NUM_LEDS):
        send_color(g, r, b)
    reset()

def cleanup():
    spi.close()
    print("SPI cleaned up")

if __name__ == "__main__":
    try:
        while True:
            # White at 20% brightness
            set_led_color(51, 51, 51)
            print("Setting LED WHITE at 20% brightness")
            time.sleep(1)
    except KeyboardInterrupt:
        cleanup()
    except Exception as e:
        print(f"An error occurred: {e}")
        cleanup()
