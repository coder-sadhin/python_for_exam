def find_top_three_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    for i in range(3):
        print(sorted_chars[i][0], sorted_chars[i][1])

input_string = input().strip()
find_top_three_characters(input_string)
