from itertools import groupby

def compress_string(s):
    compressed = []
    for key, group in groupby(s):
        count = len(list(group))
        compressed.append(f"({count}, {key})")
    return " ".join(compressed)

# Sample input
input_string = input()

# Calculate and print the modified string
print(compress_string(input_string))
