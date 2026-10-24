import sys


def helpme():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    pos = 2
    a = []
    for i in range(n):
        a.append([int(v) for v in data[pos:pos + m]])
        pos += m
    k = int(data[pos]);
    pos += 1
    p = [int(v) for v in data[pos:pos + k]]
    sig = [[0] * m for _ in range(n)]
    for i in range(n):
        row = a[i]
        s = sig[i]
        cur = 0
        for j in range(m):
            if cur > s[j]:
                s[j] = cur
            cur = max(cur - 1, row[j])
        cur = 0
        for j in range(m - 1, -1, -1):
            if cur > s[j]:
                s[j] = cur
            cur = max(cur - 1, row[j])
    for j in range(m):
        cur = 0
        for i in range(n):
            if cur > sig[i][j]:
                sig[i][j] = cur
            cur = max(cur - 1, a[i][j])
        cur = 0
        for i in range(n - 1, -1, -1):
            if cur > sig[i][j]:
                sig[i][j] = cur
            cur = max(cur - 1, a[i][j])
    cells = [(sig[i][j], i, j) for i in range(n) for j in range(m) if a[i][j] == 0]
    if len(cells) < k:
        print(-1)
        return
    cells.sort(key=lambda t: -t[0])
    order = sorted(range(k), key=lambda t: -p[t])
    res = [[0] * m for _ in range(n)]
    for t, r in enumerate(order):
        sv, i, j = cells[t]
        if sv < p[r]:
            print(-1)
            return
        res[i][j] = r + 1

    print("\n".join(" ".join(map(str, row)) for row in res))


helpme()
