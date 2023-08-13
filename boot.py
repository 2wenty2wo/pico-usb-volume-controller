import storage
import digitalio
import board

# Rotary encoder button
button = digitalio.DigitalInOut(board.GP12)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# If the knob is pressed while plugging in, enable USB drive
if button.value == 0:
    storage.remount("/", readonly=False)
else:
    storage.disable_usb_drive()