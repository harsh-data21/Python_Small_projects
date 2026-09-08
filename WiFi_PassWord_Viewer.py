"""
Day 5/75
     ...# WiFi_PassWord_Viewer #...
"""
import subprocess
import re

output = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    text=True,
    encoding="utf-8",
    errors="ignore"
)

profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)

for profile in profiles:
    profile = profile.strip()

    print(f"Wi-Fi: {profile}")
    print("-" * 40)