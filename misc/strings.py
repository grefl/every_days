def index_of(string, element_to_find, starting_index = 0):

    idx = starting_index 
    offset = len(element_to_find)
    while idx + offset - 1 < len(string):
        if string[idx : idx + offset] == element_to_find:
            return idx
        idx +=1
    return None
