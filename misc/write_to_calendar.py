from pathlib import Path
import hashlib
import datetime


def index_of(string, element_to_find, starting_index = 0):

    idx = starting_index 
    offset = len(element_to_find)
    while idx + offset - 1 < len(string):
        if string[idx : idx + offset] == element_to_find:
            return idx
        idx +=1
    return None

# -----------------------
# Put in another file
# -----------------------

def extract_string_inside_parens(due_string):
    date = None
    start = 0
    end = index_of(due_string, ')')


    return due_string[start:end] 
def parse_text(text):
    tasks      = []
    waiting_ons = []

    for line in text.split('\n'):
        if '@due' in line and '@done' not in line:
            print('@due in string')
            offset = len('@due(')
            start_from = index_of(line, '@due(') + offset
            date = extract_string_inside_parens(line[start_from:])
            if date == 'today':
                header = str(datetime.date.today()) + ':'
                task = header + '\n' + line 
                tasks.append(task)
        if '@waiting' in line and '@done' not in line:
            offset = len('@waiting(')
            start_from  = index_of(line, '@waiting(') + offset
            waiting_on = extract_string_inside_parens(line[start_from:])
            waiting_ons.append(waiting_on)

    Path('./calendar.md').write_text('\n'.join(tasks)) 
    print('finished_writing tasks to calendar')

    Path('./pingable.md').write_text('\n'.join(waiting_ons))
    print('finished_writing tasks to calendar')



modified_data_file = Path('./modified_db.txt')
last_modified, prev_hash, *rest = modified_data_file.read_text().split('\n')

file = Path('./testing.md')

file_string = file.read_text()

current_modified = file.stat().st_mtime

current_hash = hashlib.md5(file_string.encode('utf-8')).hexdigest()

if (current_modified != last_modified) and prev_hash != current_hash:
    parse_text(file_string)
    print('not the same')
else:
    print('the same')


modified_data_file.write_text(str(current_modified) + '\n' + str(current_hash))
