
EMOJIES_TABLE = {
        'heart': '❤️', 
        'smile': '🙂',
        'wink': '😉',
        'gun': '🔫'
        }

def get_emoji(name):
    if name not in EMOJIES_TABLE:
        return '🤷'
    else:
        return EMOJIES_TABLE[name]

def parse_until(string, index, condition):

    parsed_string = [] 
    found = False
    while index < len(string) and string[index] != condition and string[index] != ' ':
        parsed_string.append(string[index])
        index += 1
    if index >= len(string) or string[index] != condition:
        return None, index
    return ''.join(parsed_string), index, 

def extract_emojies(string):
    index = 0
    inside = False
    matches = []

    while index < len(string):

        if string[index] == ':' and not inside:

            inside = True
            emoji = {
                'start': index,
                'end': None,
                'name': None
            }

            emoji_name, index = parse_until(string, index + 1, ':')

            if not emoji_name:
                print('No emoji found')
                inside = False
                continue

            emoji['end']  = index
            emoji['name'] = emoji_name

            matches.append(emoji)
            inside = False

        index += 1 
    return matches 

def get_emojies(string):

    print('start')
    matches = extract_emojies(string)
    index = 0
    new_string = []
    prev_index = 0
    for match in matches:
        new_string.append(string[prev_index:match['start']])
        emoji = get_emoji(match['name'])
        new_string.append(emoji)
        prev_index = match['end'] + 1
    if matches[-1]['end'] < len(string):
        new_string.append(string[matches[-1]['end']+1:])

    print(''.join(new_string))

def main():
    string = "Hello :smile: :heart: :angry_face: :smile: you can use emojies like :gun: :wink:!"
    get_emojies(string)

if __name__ == "__main__":
    main()
