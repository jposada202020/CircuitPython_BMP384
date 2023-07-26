# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp384

i2c = board.I2C()
bmp = bmp384.BMP384(i2c)

bmp.filter_coefficients = bmp384.IIR_FILTER_X32

while True:
    for filter_coefficients in bmp384.filter_coefficients_values:
        print("Current Filter coefficients setting: ", bmp.filter_coefficients)
        for _ in range(10):
            print(f"Pressure: {bmp.pressure:.2f}hPa")
            print()
            time.sleep(0.5)
        bmp.filter_coefficients = filter_coefficients
