#!/usr/bin/python3
import os
import glob
import time
import subprocess
import signal
import sys

def signal_handler(sig, frame):
    print("\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
files = {}

while True:
    for name in glob.glob("*.cpp"):
        stats = os.stat(name)
        if name in files:
            old_time = files[name]["timestamp"]
            new_time = stats.st_mtime
            if new_time != old_time:
                # check if file as either is worth compiling or not
                compile = subprocess.call("g++ {} -Wall -fsyntax-only >/dev/null 2>&1".format(files[name]["cpp"]),shell=True)
                if compile == 0:
                    print("\033[92m[{}] Compiling {}\033[0m".format(time.strftime("%H:%M:%S"),files[name]["cpp"]))
                    subprocess.call("timeout 5 g++ -g {} -Wall -o {} && ./{}".format(files[name]["cpp"],files[name]["program"],files[name]["program"]), shell=True)
            files[name]["timestamp"] = new_time
        else:
            files[name] = { "timestamp": stats.st_mtime, 
                            "cpp": name,
                            "program": os.path.splitext(name)[0]
                            }
            print("adding {}".format(files[name]))
    time.sleep(0.5)
        
