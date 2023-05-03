# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`bmp384`
================================================================================

CircuitPython Driver for the Bosch BMP384 Pressure and Temperature sensor


* Author(s): Jose D. Montoya


"""

from micropython import const
from adafruit_bus_device import i2c_device
from adafruit_register.i2c_struct import ROUnaryStruct, UnaryStruct
from adafruit_register.i2c_bits import RWBits

try:
    from busio import I2C
    from typing import Tuple
except ImportError:
    pass


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/jposada202020/CircuitPython_BMP384.git"

_REG_WHOAMI = const(0x00)
_PWR_CTRL = const(0x1B)

SLEEP_MODE = const(0b00)
FORCED_MODE = const(0b10)
NORMAL_MODE = const(0b11)
power_mode_values = (SLEEP_MODE, FORCED_MODE, NORMAL_MODE, )

class BMP384:
    """Driver for the BMP384 Sensor connected over I2C.

    :param ~busio.I2C i2c_bus: The I2C bus the BMP384 is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x77`

    :raises RuntimeError: if the sensor is not found

    **Quickstart: Importing and using the device**

    Here is an example of using the :class:`BMP384` class.
    First you will need to import the libraries to use the sensor

    .. code-block:: python

        import board
        import bmp384

    Once this is done you can define your `board.I2C` object and define your sensor object

    .. code-block:: python

        i2c = board.I2C()  # uses board.SCL and board.SDA
        bmp = bmp384.BMP384(i2c)

    Now you have access to the attributes

    .. code-block:: python

        press = bmp.pressure
        temp = bmp.temperature

    """

    _device_id = ROUnaryStruct(_REG_WHOAMI, "B")

    _operation_mode = RWBits(2, _PWR_CTRL,4)

    def __init__(self, i2c_bus: I2C, address: int = 0x77) -> None:
        self.i2c_device = i2c_device.I2CDevice(i2c_bus, address)

        if self._device_id != 0x50:
            raise RuntimeError("Failed to find BMP384")