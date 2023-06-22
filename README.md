# Raspberry Pi Pico Arcade Control: Volume & Game Exit Controller

This project is a custom controller for an arcade or MAME cabinet that allows the player to control the volume and exit the current game using a Raspberry Pi Pico, a rotary encoder, and an extra pushbutton. The volume is controlled by rotating the knob on the encoder, pressing the knob mutes the volume, and pressing the extra button sends an Alt+Ctrl+F4 command to exit the game.

## Prerequisites

To build and use this controller, you will need:

- A Raspberry Pi Pico.
- Adafruit's CircuitPython firmware installed on the Pico. You can find installation instructions [here](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/install-circuitpython).
- A rotary encoder with a built-in switch. We used [this](https://core-electronics.com.au/encoder-module-with-button.html) one in our setup.
- An additional pushbutton switch.
- A PC running the SuperF4 program, which can be downloaded from [here](https://stefansundin.github.io/superf4/).

## Wiring

Make the following connections between the Pico, the rotary encoder, and the pushbutton:

- The encoder's A (S1) output to the Pico's GP10 pin.
- The encoder's B (S2) output to the Pico's GP9 pin.
- The encoder's switch (Key) output to the Pico's GP12 pin.
- The additional pushbutton switch to the Pico's GP13 pin.

Remember to also connect the ground and power lines of the encoder and pushbutton to the ground and 3.3V pins on the Pico, respectively.

## Usage

The controller works as follows:

- Rotate the knob clockwise to increase the volume.
- Rotate the knob counterclockwise to decrease the volume.
- Press the knob to mute and unmute the audio.
- Press the extra pushbutton to send the Alt+Ctrl+F4 command, which will trigger SuperF4 to exit the current game.

## Code

The Python script `main.py` in this repository contains the code that runs on the Pico. It uses the `rotaryio`, `usb_hid`, and `adafruit_hid` libraries to read the encoder and pushbutton inputs and send HID commands to the PC.

## Credits

This project was generated with the help of OpenAI's ChatGPT. It uses the `adafruit_hid` library and was inspired by Adafruit's [rotary encoder tutorial](https://learn.adafruit.com/rotary-encoder-in-circuitpython/overview) and this [blog post](https://blog.thestaticturtle.fr/2021/02/11/getting-started-with-hid-and-the-pi-pico/) on HID with the Pi Pico.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
