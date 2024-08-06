import lgpio
import time

# Configuration
LED_PIN = 21  # GPIO pin connected to the data pin of the WS2812B
NUM_LEDS = 300  # Number of LEDs in the strip

# Timing constants (in nanoseconds)
T0H = 400  # 0.4us
T0L = 850  # 0.85us
T1H = 800  # 0.8us
T1L = 450  # 0.45us
RESET_TIME = 50000  # Reset signal low for 50us

# Setup GPIO
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED_PIN)

def send_bit(bit):
    if bit == 1:
        lgpio.gpio_write(h, LED_PIN, 1)
        lgpio.gpio_sleep(h, 0, T1H)
        lgpio.gpio_write(h, LED_PIN, 0)
        lgpio.gpio_sleep(h, 0, T1L)
    else:
        lgpio.gpio_write(h, LED_PIN, 1)
        lgpio.gpio_sleep(h, 0, T0H)
        lgpio.gpio_write(h, LED_PIN, 0)
        lgpio.gpio_sleep(h, 0, T0L)

def send_byte(byte):
    for i in range(8):
        send_bit((byte >> (7 - i)) & 1)

def send_color(g, r, b):
    send_byte(g)
    send_byte(r)
    send_byte(b)

def reset():
    lgpio.gpio_write(h, LED_PIN, 0)
    lgpio.gpio_sleep(h, 0, RESET_TIME)

# Main function
def set_led_color(r, g, b):
    for _ in range(NUM_LEDS):
        send_color(g, r, b)
    reset()

if __name__ == "__main__":
    try:
        while True:
            # White at 20% brightness
            set_led_color(51, 51, 51)
            print("Setting LED WHITE at 20% brightness")
            time.sleep(1)
    except KeyboardInterrupt:
        lgpio.gpiochip_close(h)
    except Exception as e:
        print(f"An error occurred: {e}")
        lgpio.gpiochip_close(h)
