import time
import board
import usb_hid
import digitalio
import rotaryio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Configuration
DEBUG = False
DEBOUNCE_DELAY = 0.01
ROTARY_ENCODER_PINS = (board.GP9, board.GP10)
BUTTON_PIN = board.GP12
MACRO_BUTTON_PIN = board.GP13
MACRO_ACTION = "ALT_CTRL_F4"  # Options: "ESC" or "ALT_CTRL_F4"

# Initialize HID devices
cc = ConsumerControl(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)

# Rotary encoder setup
encoder = rotaryio.IncrementalEncoder(*ROTARY_ENCODER_PINS)
last_position = encoder.position

# Rotary encoder button setup
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None

# Additional button setup for Alt+Ctrl+F4 or ESC
macro_button = digitalio.DigitalInOut(MACRO_BUTTON_PIN)
macro_button.direction = digitalio.Direction.INPUT
macro_button.pull = digitalio.Pull.UP

# Function to handle volume control
def handle_volume(position_change):
    if position_change > 0:
        for _ in range(position_change):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif position_change < 0:
        for _ in range(-position_change):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)

# Function to initialize HID devices
def initialize_hid_devices():
    global cc, kbd
    cc = ConsumerControl(usb_hid.devices)
    kbd = Keyboard(usb_hid.devices)

# Function to handle button actions
def handle_buttons():
    global button_state
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        cc.send(ConsumerControlCode.MUTE)
        button_state = None
    if not macro_button.value:
        if MACRO_ACTION == "ESC":
            kbd.send(Keycode.ESCAPE)
        else:
            kbd.send(Keycode.ALT, Keycode.CONTROL, Keycode.F4)

# Main loop
initialize_hid_devices()  # Initial initialization of HID devices
while True:
    # Handle volume control
    current_position = encoder.position
    position_change = current_position - last_position
    handle_volume(position_change)
    last_position = current_position

    # Handle button actions
    handle_buttons()

    # Periodically reinitialize HID devices
    if cc is None or kbd is None:
        initialize_hid_devices()

    time.sleep(DEBOUNCE_DELAY)  # debounce delay