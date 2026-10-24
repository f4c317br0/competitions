import sys


def zxc():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    g = data[2:2 + n]
    cells = [(i, j) for i in range(n) for j in range(m) if g[i][j] == '#']
    cnt = len(cells)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for X in range(3, 61):
        if X * (X + 1) // 2 < cnt:
            continue
        for (sr, sc) in cells:
            for d0 in range(4):
                for s in (1, -1):
                    r, c, di = sr, sc, d0
                    x = X
                    seen = set()
                    ok = True
                    while x > 0 and ok:
                        dr, dc = dirs[di]
                        for t in range(x):
                            if not (0 <= r < n and 0 <= c < m) or g[r][c] != '#':
                                ok = False
                                break
                            seen.add((r, c))
                            if t < x - 1:
                                r += dr
                                c += dc
                        if not ok:
                            break
                        x -= 1
                        if x == 0:
                            break
                        nd = (di + s) % 4
                        r += dr + dirs[nd][0]
                        c += dc + dirs[nd][1]
                        di = nd
                    if ok and len(seen) == cnt:
                        print(("CW" if s == 1 else "CCW"), X)
                        return


zxc()
