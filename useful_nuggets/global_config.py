import os

SYSTEM_GLOBAL_ENV = None

if os.getenv("YOUR_GLOBAL_ENV") == "I_EXIST":
    SYSTEM_GLOBAL_ENV = True

def do_thing():
    if SYSTEM_GLOBAL_ENV:
        print('yup')

