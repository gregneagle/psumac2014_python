#!/usr/bin/python

"""Calls system_profiler and prints hardware info about
the current machine"""

import plistlib
import subprocess

cmd = ['/usr/sbin/system_profiler', 'SPHardwareDataType', '-xml']
output = subprocess.check_output(cmd)

info = plistlib.readPlistFromString(output)

hardware_info = info[0]['_items'][0]
for key, value in hardware_info.items():
    print str(key) + ": " + str(value)
