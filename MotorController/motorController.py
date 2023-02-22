#!/usr/bin/env python3
""" A stepper motor controller script for the Raspberry Pi.

This script is designed to control a stepper motor using the Raspberry Pi. 
It will take a frequency input and use that to control the speed of the motor.
"""


import RPi.GPIO as GPIO  # Import the GPIO library.
from time import sleep
import sys

__author__ = "Kyle Wiskel"
__copyright__ = "Copyright 2023, MMA project"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Kyle Wiskel"
__email__ = "wiskel@ualberta.ca"
__status__ = "Development"


# Define GPIO pins
motor_channel = (29, 31, 33, 35)
GPIO.setwarnings(False)  # disable warnings
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering


class ControlMotor(frequency):
    """This class will control the stepper motor based on the frequency input.

    frequency: The frequency of the motor in Hz.
    """

    pass
