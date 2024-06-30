import re
A = input()
B = input()
matches = list(re.finditer(r'(?={})'.format(re.escape(B)), A))
if not matches:
    print((-1, -1))
else:
    # Otherwise, print the start and end indices of each match
    for match in matches:
        start_index = match.start()
        end_index = start_index + len(B) - 1
        print((start_index, end_index))
