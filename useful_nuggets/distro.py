#!/bin/env python3
import subprocess


def parse_to_end(bytestring):
    """
    Gets all the chars from the byte string until it reaches the end.
    Is it pythonic, heck no! But I don't care since it works and I'm just experimenting.
    """
    idx = 0
    string = []
    while idx < len(bytestring):
        c = chr(bytestring[idx])
        idx +=1
        if c == '\n':
            continue
        string.append(c)
    return ''.join(string)

def distro_id():
    """
    Gets the distro id. In my case, it prints -> "Pop" since I'm on Pop os
    """

    cmd = ("lsb_release", "-i")
    stdout = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)

    # The length of "Distributor ID:\t" is 16.
    # So we should start collecting the chars from this index.
    index = len(b'Distributor ID:\t')
    print(parse_to_end(stdout[index:]))


distro_id()