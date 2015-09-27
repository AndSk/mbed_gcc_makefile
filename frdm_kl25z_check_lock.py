#!/usr/bin/env python3

import sys
import os

with open(sys.argv[1], "rb") as fd:
    fd.seek(0x0000040C)
    lockbits = fd.read(1)[0] & 0x03
    if lockbits != 0x02:
        print("Lockbits are set up to lock your device. You must not flash this image!")
        os.unlink(sys.argv[1])
        sys.exit(1)
