import subprocess
cmd = ['/usr/sbin/system_profiler', 'SPHardwareDataType', '-xml']
proc = subprocess.call(cmd)


proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(output, error) = proc.communicate()
print output


import plistlib
info = plistlib.readPlistFromString(output)
info


hardware_info = info[0]['_items'][0]
hardware_info.keys()


hardware_info['cpu_type']
hardware_info['machine_model']
hardware_info['serial_number']


for key, value in hardware_info.items():
    print str(key) + ": " + str(value)
