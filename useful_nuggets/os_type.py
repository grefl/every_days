import sys 
import os

LINUX   = sys.platform.startswith("linux")
WINDOWS = os.name == "nt"
MACOS   = sys.platform.startswith("darwin") 

if LINUX:
    print("It's linux")
elif WINDOWS:
    print("It's windows")
elif MACOS:
    print("It's macos")
