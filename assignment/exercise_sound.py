#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    if frequency == 0:
        quiet()
    else:
        speaker.duty_u16(1000)
        speaker.freq(frequency)
    utime.sleep(duration)
    quiet()


def quiet():
    speaker.duty_u16(0)


# Frequencies for the main melody of the Super Mario Bros theme
melody = [
    659, 659, 0, 659, 0, 523, 659, 0, 784, 0, 0, 0, 392, 0, 0, 0,
    523, 0, 0, 392, 0, 0, 330, 0, 0, 440, 0, 494, 466, 440, 0,
    523, 0, 659, 784, 0, 698, 740, 0, 0, 659, 0, 523, 587, 494, 0,
    523, 0, 392, 0, 330, 0, 440, 494, 466, 440, 0, 523, 0, 659, 784, 0,
    698, 740, 0, 0, 659, 0, 523, 587, 494, 0, 0
]

# Durations for each note (in seconds)
durations = [
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
    0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15
]

print("Playing Super Mario Bros theme:")

for freq, dur in zip(melody, durations):
    print(f"Playing frequency (Hz): {freq}")
    playtone(freq, dur)

# Turn off the PWM
quiet()