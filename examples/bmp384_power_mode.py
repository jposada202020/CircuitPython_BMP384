# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp384

i2c = board.I2C()
bmp = bmp384.BMP384(i2c)

bmp.power_mode = bmp384.NORMAL_MODE

while True:
    for power_mode in bmp384.power_mode_values:
        print("Current Power mode setting: ", bmp.power_mode)
        for _ in range(10):
            print(f"Pressure: {bmp.pressure:.2f}hPa")
            print()
            time.sleep(0.5)
        bmp.power_mode = power_mode
