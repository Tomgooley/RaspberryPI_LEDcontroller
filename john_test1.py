import lgpio
import time

# Configuration
LED_PIN = 21  # GPIO pin connected to the data pin of the WS2812B
NUM_LEDS = 300  # Number of LEDs in the strip

# Timing constants (in seconds)
T0H = 0.0000004  # 0.4us
T0L = 0.00000085  # 0.85us
T1H = 0.0000008  # 0.8us
T1L = 0.00000045  # 0.45us
RESET_TIME = 0.00005  # Reset signal low for 50us

# Setup GPIO
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED_PIN)

def send_bit(bit):
    if bit == 1:
        lgpio.gpio_write(h, LED_PIN, 1)
        time.sleep(T1H)
        lgpio.gpio_write(h, LED_PIN, 0)
        time.sleep(T1L)
    else:
        lgpio.gpio_write(h, LED_PIN, 1)
        time.sleep(T0H)
        lgpio.gpio_write(h, LED_PIN, 0)
        time.sleep(T0L)

def send_byte(byte):
    for i in range(8):
        send_bit((byte >> (7 - i)) & 1)

def send_color(g, r, b):
    send_byte(g)
    send_byte(r)
    send_byte(b)

def reset():
    lgpio.gpio_write(h, LED_PIN, 0)
    time.sleep(RESET_TIME)

# Main function
def set_led_color(r, g, b):
    for _ in range(NUM_LEDS):
        send_color(g, r, b)
    reset()

def cleanup():
    lgpio.gpiochip_close(h)
    print("GPIO cleaned up")

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
