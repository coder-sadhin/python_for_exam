if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    sorted_athletes = sorted(arr, key=lambda x: x[k])

    # Print the sorted table
    for athlete in sorted_athletes:
        print(*athlete)
