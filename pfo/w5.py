import sys

data = sys.stdin.read().split()
n = int(data[0])
g = data[1:1 + n]
x = int(data[1 + n]) - 1
y = int(data[2 + n]) - 1
z = int(data[3 + n]) - 1
a = int(g[x][y])
b = int(g[y][z])
d = int(g[z][x])
seed = {a: [z, x], b: [x, y], d: [y, z]}
out = []
for c in (1, 2, 3):
    S = list(seed.get(c, []))
    ch = str(c)
    for v in range(n):
        if v in S:
            continue
        if all(g[v][u] != ch for u in S):
            S.append(v)
    out.append(str(len(S)) + " " + " ".join(str(v + 1) for v in S))
print("\n".join(out))
