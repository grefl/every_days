from shutil import which


# You can import which from shutil which is super handy

def my_which(cmd):
    # will return the path or None
    return which(cmd)


print(my_which('python3'))
