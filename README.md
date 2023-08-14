# Pico USB Volume Controller for Arcade/MAME Machines

![Pico USB Volume Controller in action](https://github.com/2wenty2wo/pico-usb-volume-controller/blob/main/picture.gif?raw=true)

Elevate your arcade/MAME machine experience with a seamless volume control and game exit solution using the Raspberry Pi Pico and a rotary encoder.

---

## 📌 Table of Contents
- [🎮 Introduction](#introduction)
- [✨ Features](#features)
- [📦 Requirements](#requirements)
- [🚀 Setup and Installation](#setup-and-installation)
- [🔌 Hardware and Wiring](#hardware-and-wiring)
- [⚙️ Configuration](#configuration)
- [📚 Resources](#resources)
- [📜 Code Base Source](#code-base-source)
- [🙏 Acknowledgements](#acknowledgements)

---

## 🎮 Introduction

Arcade/MAME machines, especially those running on Windows platforms, often lack intuitive controls for volume adjustment or game exit. This project bridges that gap, offering a tactile and user-friendly solution. With a Raspberry Pi Pico and a rotary encoder, you can now seamlessly manage volume levels and exit games directly from your arcade cabinet's control panel. This ensures a more immersive and uninterrupted gaming experience.

---

## ✨ Features

- **🔊 Volume Control**: A simple twist of the encoder adjusts the volume, giving you the perfect audio balance for your gaming sessions.
- **🔇 Mute Feature**: A quick press mutes and unmutes, ensuring you can quickly silence your games when needed.
- **🚪 Exit Games**: An additional button sends the `ALT + CTRL + F4` command, swiftly exiting games and ensuring you can quickly switch between games or take a break.
- **🖥️ HID Integration**: The Raspberry Pi Pico naturally acts as a HID when connected, ensuring smooth integration with your setup and making it a plug-and-play solution.

---

## 📦 Requirements

- **Hardware**:
  - Raspberry Pi Pico: A versatile microcontroller that serves as the brain of this project.
  - Rotary Encoder (with a push button): Provides tactile feedback for volume control and muting.
  - Optional push button (for the `ALT + CTRL + F4` feature): A dedicated button for swift game exits.
  
- **Software**:
  - [SuperF4](https://stefansundin.github.io/superf4/): A lightweight software that ensures a smooth game exit experience, preventing accidental exits to the Windows desktop.

---

## 🚀 Setup and Installation

1. **CircuitPython**: Begin by flashing your Raspberry Pi Pico with CircuitPython. This provides a Python environment on your Pico, making it compatible with our scripts. [Here's a step-by-step guide](https://circuitpython.org/board/raspberry_pi_pico/).
2. **Code Transfer**: Drag and drop the `boot.py` and `code.py` files onto your Raspberry Pi Pico. These scripts contain the logic for volume control and game exits.
3. **SuperF4 Setup**: Install [SuperF4](https://stefansundin.github.io/superf4/) on your arcade machine. Once installed, tweak the settings to optimize game exits, ensuring a seamless transition between games.

---

## 🔌 Hardware and Wiring

**Components**:
- Raspberry Pi Pico: The microcontroller that interprets and sends commands.
- Rotary Encoder (with a push button): The main interface for volume control.
- Optional push button for game exits: A dedicated button for swift game transitions.

**Wiring Guide**:
- **Rotary Encoder**:
  - `A (S1) Pin` -> `GP9` on Pico
  - `B (S2) Pin` -> `GP10` on Pico
  - `SW (Key) Pin` -> `GP12` on Pico
  - `+ Pin` -> `3.3V` on Pico
  - `GND Pin` -> `GND` on Pico
  
- **Game Exit Button**:
  - One end -> `GP13` on Pico
  - Other end -> `GND` on Pico

---

## ⚙️ Configuration

Dive into the `code.py` file to find a configuration section at the top. This section is designed for easy customization, allowing you to tailor the experience to your preferences. Whether it's adjusting debounce delays or changing pin assignments, this section ensures your setup works perfectly for your specific arcade machine.

---

## 📚 Resources

- [Raspberry Pi Pico Documentation](https://www.raspberrypi.org/documentation/rp2040/getting-started/): Comprehensive documentation covering everything you need to know about the Raspberry Pi Pico.
- [SuperF4 Official Page](https://stefansundin.github.io/superf4/): Learn more about SuperF4 and its features.

---

## 📜 Code Base Source

A shoutout to the [multimedia-knob](https://github.com/Xitee1/multimedia-knob) repository by [Xitee1](https://github.com/Xitee1). This project was inspired by their innovative approach to multimedia control using a rotary encoder and Raspberry Pi Pico. Their foundational work provided a stepping stone for this project.

---

## 🙏 Acknowledgements

A big thank you to ChatGPT by OpenAI for enhancing this project's documentation. Their insights and suggestions played a pivotal role in making this README comprehensive and user-friendly.
