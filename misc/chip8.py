from font import font
# Goals
# 1. Understand chip8
# 2. Implement a rough pseudocode of the basic parts of chip8
# 3. Anything else is bonus.

# Program counter
PC = 0
# Index register 16bits
I = 0

# 16 * 8bit registers
# V0->VF
reg = bytearray(16) 

# Memory 4 kilobytes or 4096 bytes
# Notes on memory
# 1. original CHIP-8 interpreters expected the first 511 bytes to be 
# filled with the interpretor. As such you should mark 0x00-0x1FF as not being unsused.
memory = bytearray(4096) 

# Font
# Represent hexadecimal characters from 0-F
# Each font character should be 4 pixels wide by 5 pixels tall.
font_index = 0
for i in range(0x050, 0x050 + len(font)):
    memory[i] = font[font_index]
    font_index += 1
# assert that start and end font are as there
assert(memory[0x050] == 0xF0)    
assert(memory[0x050+len(font) - 1] == 0x80)    

# Display
# 64x32
# Each pixel is either on or off - boolean


# Stack
# used for saving the 16bit address of subroutines
# Most stacks are limited to 16 2byte entries
# indexing should be i * 2
stack = bytearray(16*2) 

# Timers
# 1. delay time
# 2. sound timer
# both count down to zero 60 times a second

# Keypad
# goes from 0x0-0xF

# Fetch/decode/execute loop

def timer(cb):
    # counts down to zero
    # run this 60 times a second?
    cb()
def sound_timer(cb):
    # counts down to zero
    # gives off sound unless we have reached 0
    # run this 60 times a second?

    cb()
def chip8():
    pass
if __name__ == "__main__":
    chip8()
