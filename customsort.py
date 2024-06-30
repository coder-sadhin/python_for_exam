def custom_sort(s):
    sorted_string = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))
    return ''.join(sorted_string)

# Input
input_string = input().strip()

# Calculate and print the sorted string
print(custom_sort(input_string))
