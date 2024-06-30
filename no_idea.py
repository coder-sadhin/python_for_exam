def calculate_happiness(arr, like_set, dislike_set):
    total_happiness = 0
    for num in arr:
        if num in like_set:
            total_happiness += 1
        elif num in dislike_set:
            total_happiness -= 1
    return total_happiness

# Sample input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
like_set = set(map(int, input().split()))
dislike_set = set(map(int, input().split()))

# Calculate and print the final happiness
print(calculate_happiness(arr, like_set, dislike_set))
