import time
import board
import usb_hid
import digitalio
import rotaryio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Setup the rotary encoder button
button = digitalio.DigitalInOut(board.GP12)  # Encoder module "Key" connected to GP12
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Setup the additional pushbutton for Alt+Ctrl+F4
macro_button = digitalio.DigitalInOut(board.GP13)  # Additional button connected to GP13
macro_button.direction = digitalio.Direction.INPUT
macro_button.pull = digitalio.Pull.UP

# Setup the rotary encoder
encoder = rotaryio.IncrementalEncoder(board.GP10, board.GP9)  # Encoder A (S1) connected to GP10, Encoder B (S2) connected to GP9

# Setup the HID devices
cc = ConsumerControl(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)

button_state = None
macro_button_state = None
last_position = encoder.position

while True:
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif position_change < 0:
        for _ in range(-position_change):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    last_position = current_position

    # Check the state of the rotary encoder button
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        cc.send(ConsumerControlCode.MUTE)
        button_state = None

    # Check the state of the macro button
    if not macro_button.value and macro_button_state is None:
        macro_button_state = "pressed"
    if macro_button.value and macro_button_state == "pressed":
        kbd.send(Keycode.ALT, Keycode.CONTROL, Keycode.F4)
        macro_button_state = None
    time.sleep(0.01)  # debounce delay
