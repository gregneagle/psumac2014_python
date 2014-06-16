import sys
sys.platform


import os
os.uname()
os.uname()[2]
os.uname()[4]


import platform
platform.mac_ver()
platform.mac_ver()[0]


import subprocess
cmd = ['/usr/bin/sw_vers', '-productVersion']
subprocess.check_output(cmd)

subprocess.check_output(cmd).strip()
