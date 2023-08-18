# Pico USB Volume Controller for Arcade/MAME Machines

![Pico USB Volume Controller in action](https://github.com/2wenty2wo/pico-usb-volume-controller/blob/main/picture.gif?raw=true)

Control volume and exit games with ease using the Raspberry Pi Pico and a rotary encoder.

---

## 📌 Table of Contents
- [🕹 Introduction](#introduction)
- [✨ Features](#features)
- [📦 Requirements](#requirements)
- [🚀 Setup and Installation](#setup-and-installation)
- [🔌 Hardware and Wiring](#hardware-and-wiring)
- [⚙️ Configuration](#configuration)
- [📚 Resources](#resources)
- [📝 Code Base Source](#code-base-source)

---

## 🕹 Introduction

This project provides a simple and effective solution for volume control and game exit functionality for Arcade/MAME machines using a Raspberry Pi Pico and a rotary encoder.

---

## ✨ Features

- **🔊 Volume Control**: Twist the encoder to adjust the volume.
- **🔇 Mute Feature**: A quick press mutes and unmutes the audio.
- **🚪 Exit Games**: An additional button sends the `ALT + CTRL + F4` command to exit games.
- **🔍 HID Integration**: The Raspberry Pi Pico acts as a HID when connected, making it a plug-and-play solution.

---

## 📦 Requirements

- **Hardware**:
  - Raspberry Pi Pico
  - Rotary Encoder (with a push button)
  - Optional push button (for the `ALT + CTRL + F4` feature)
  
- **Software**:
  - [SuperF4](https://stefansundin.github.io/superf4/)

---

## 🚀 Setup and Installation

1. **CircuitPython**: Flash your Raspberry Pi Pico with CircuitPython. [Guide](https://circuitpython.org/board/raspberry_pi_pico/).
2. **Code Transfer**: Drag and drop the `boot.py` and `code.py` files onto your Raspberry Pi Pico.
3. **Lib Folder**: Copy over the `lib` folder to your Raspberry Pi Pico.
4. **SuperF4 Setup**: Install [SuperF4](https://stefansundin.github.io/superf4/) on your arcade machine.

---

## 🔌 Hardware and Wiring

**Components**:
- Raspberry Pi Pico
- Rotary Encoder (with a push button)
- Optional push button for game exits

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

Check the `code.py` file for a configuration section at the top. Customize debounce delays, pin assignments, and more to fit your setup.

---

## 📚 Resources

- [Raspberry Pi Pico Documentation](https://www.raspberrypi.org/documentation/rp2040/getting-started/)
- [SuperF4 Official Page](https://stefansundin.github.io/superf4/)

---

## 📝 Code Base Source

Inspired by the [multimedia-knob](https://github.com/Xitee1/multimedia-knob) repository by [Xitee1](https://github.com/Xitee1).
