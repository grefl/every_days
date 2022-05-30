import subprocess

def parse_to_end(bytestring):
    idx = 0
    string = []
    while idx < len(bytestring):
        string.append(chr(bytestring[idx]))
        idx +=1
    return ''.join(string)

def id():
    cmd = ("lsb_release", "-i")
    print(len(b'Distributor ID:\t'))
    stdout = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    index = 16
    print(parse_to_end(stdout[index:]))


id()

