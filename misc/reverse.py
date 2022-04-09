def reverse(string):
    mid = (len(string) -1) / 2
    string_builder = [None] * len(string) 
    sl = len(string)-1
    i = 0
    while i <= mid:
        string_builder[i] = string[sl-i] 
        string_builder[sl-i] = string[i]
        i +=1
    print(string_builder)
    return "".join(string_builder)



test_string = "Well, hello there" 
print(reverse(test_string) == test_string[::-1])
