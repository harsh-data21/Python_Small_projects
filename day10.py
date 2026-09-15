"""
Day = 10

"""

import subprocess

output = subprocess.run(
    "netsh wlan show interfaces",
    shell=True,
    capture_output=True,
    text=True
)

print(output.stdout)

if output.returncode != 0:
    print("Error:")
    print(output.stderr)