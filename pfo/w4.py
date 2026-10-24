import sys
from collections import Counter

data = sys.stdin.buffer.read().split()
n = int(data[0])
xs = data[1:2 * n + 1:2]
ys = data[2:2 * n + 2:2]
pts = [(int(a), int(b)) for a, b in zip(xs, ys)]
cd = Counter()
cs = Counter()
cp = [0, 0]
for x, y in pts:
    cd[x - y] += 1
    cs[x + y] += 1
    cp[(x + y) & 1] += 1
res = []
for x, y in pts:
    c = cp[(x + y) & 1]
    d = cd[x - y] - 1 + cs[x + y] - 1
    res.append(2 * (c - 1) - d)
print(" ".join(map(str, res)))
