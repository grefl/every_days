import sys 
# import os

platform = sys.platform
LINUX    = platform.startswith("linux") 
# WINDOWS = os.name == "nt"
WINDOWS  = platform.startswith("win32") or platform.startswith("cywin") 
MACOS    = platform.startswith("darwin") 

if LINUX:
    print("It's linux")
elif WINDOWS:
    print("It's windows")
elif MACOS:
    print("It's macos")
