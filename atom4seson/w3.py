import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    successful_hits = 0
    idx = 1
    for _ in range(n):
        x = float(input_data[idx])
        y = float(input_data[idx + 1])
        idx += 2
        abs_x = abs(x)
        if (y <= 4 - abs_x and abs_x <= 4 and y >= -2 and y >= abs_x - 5):
            if abs_x < 1 and -1 < y < 2 - abs_x:
                continue
            successful_hits += 1

    print(successful_hits)


solve()
