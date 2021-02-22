# How to restore MAC address

import subprocess

subprocess.call("ethtool -P eth0", shell=True)
subprocess.call("sudo ifconfig eth0 hw ether $(ethtool -P eth0 | awk '{print $3}')", shell=True)


