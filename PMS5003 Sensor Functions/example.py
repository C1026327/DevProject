# !/usr/bin/env python
##import os
##bash = "source ~/.virtualenvs/pimoroni/bin"
##os.system(bash)
from pms5003 import PMS5003
print(
    """all.py - Continuously print all data values.
Press Ctrl+C to exit!
"""
)
# Recognise device and library
pms5003 = PMS5003(device="/dev/serial0", baudrate=9600)
# Print all data accessed by device
try:
    while True:
        data = pms5003.read()
        print(data)
# Stop Program
except KeyboardInterrupt:
    pass
