

def replace_spaces(string):
    spaces = 0
    for c in string:
        if c == ' ':
            spaces +=1
    spaced_string = [None] * (len(string) + (2* spaces)) 
    print(spaced_string)
    index= len(spaced_string)
    for i in reversed(range(len(string))):
        print(i, len(string))
        if string[i] == ' ':
            spaced_string[index-1] = '0'
            spaced_string[index-2] = '2'
            spaced_string[index-3] = '%'
            index = index - 3
        else:
            spaced_string[index-1] = string[i] 
            index -=1
        spaced_string
    return ''.join(spaced_string)
print(replace_spaces("mesa jar jar binks"))

