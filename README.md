# Pico USB Volume Controller for Arcade/MAME Machines

Control the volume and exit games on your arcade/MAME machine using a Raspberry Pi Pico and a rotary encoder.

![Picture](https://github.com/2wenty2wo/pico-usb-volume-controller/blob/main/picture.gif?raw=true)

## Introduction

Arcade/MAME machines running on Windows often lack an intuitive way to control the volume or exit games without diving into the software or using complex key combinations. This project provides a simple and elegant solution by using a Raspberry Pi Pico and a rotary encoder. With this setup, you can easily control the volume and exit games directly from your arcade cabinet's control panel.

## Features

- **Volume Control**: Turn the rotary encoder to increase or decrease the volume.
- **Mute**: Press the rotary encoder to mute/unmute the volume.
- **Exit Games**: An additional button can be configured to send the `ALT + CTRL + F4` key combination, which, when used with [SuperF4](https://stefansundin.github.io/superf4/), can kill the game and return you to your frontend. SuperF4 settings can be adjusted to blacklist the frontend, ensuring users can only exit games and not access the Windows desktop.
- **HID Device**: By default, the Raspberry Pi Pico will only show up as a HID (Human Interface Device) when connected to a computer. This means it won't appear as a USB drive unless the rotary encoder knob is pressed while plugging it in, ensuring a seamless experience.

## Requirements

- Raspberry Pi Pico
- Rotary Encoder with a push button
- Additional push button (optional for the `ALT + CTRL + F4` feature)
- [SuperF4](https://stefansundin.github.io/superf4/) software installed on your arcade machine

## Setup and Installation

1. **Flash MicroPython**: If you haven't already, flash your Raspberry Pi Pico with MicroPython. Instructions can be found [here](https://www.raspberrypi.org/documentation/rp2040/getting-started/#getting-started-with-micropython).
2. **Upload the Code**: Copy the `boot.py` and `code.py` files to your Raspberry Pi Pico.
3. **Install SuperF4**: Download and install [SuperF4](https://stefansundin.github.io/superf4/) on your arcade machine. Adjust the settings to blacklist your frontend, ensuring users can only exit games.

## Hardware and Wiring

### Components:

- Raspberry Pi Pico
- Rotary Encoder with a push button
- Additional push button (optional)

### Wiring:

- **Rotary Encoder**:
  - `A (S1) Pin` -> `GP9` on Pico
  - `B (S2) Pin` -> `GP10` on Pico
  - `SW (Key) Pin` -> `GP12` on Pico
  - `+ Pin` -> `3.3V` on Pico
  - `GND Pin` -> `GND` on Pico
- **Additional Push Button**:
  - One end -> `GP13` on Pico
  - Other end -> `GND` on Pico

## Configuration

The `code.py` file contains a configuration section at the top, allowing you to easily customize the behavior:

- `DEBUG`: Enables or disables debug mode.
- `DEBOUNCE_DELAY`: Adjusts the debounce delay for the buttons.
- `ROTARY_ENCODER_PINS`: Defines the pins connected to the rotary encoder.
- `BUTTON_PIN`: Defines the pin connected to the rotary encoder's push button.
- `MACRO_BUTTON_PIN`: Defines the pin connected to the additional push button.
- `MACRO_ACTION`: Determines the action of the macro button. Options are "ESC" or "ALT_CTRL_F4".

## Resources

- [Raspberry Pi Pico Documentation](https://www.raspberrypi.org/documentation/rp2040/getting-started/)
- [SuperF4](https://stefansundin.github.io/superf4/)

## Code Base Source

The foundational code and concept were derived from the [multimedia-knob](https://github.com/Xitee1/multimedia-knob) repository by [Xitee1](https://github.com/Xitee1). This repository provided an excellent starting point, showcasing how a rotary encoder can be used with a Raspberry Pi Pico for multimedia control.

## Acknowledgements

This project was crafted with the assistance of ChatGPT by OpenAI.
