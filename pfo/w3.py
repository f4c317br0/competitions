import sys
import numpy as np

mod = 998244353
T = 200
data = sys.stdin.buffer.read().split()
s = data[0].decode()
q = int(data[1])
m = len(s)
vals = np.array(list(map(int, data[2:2 + 2 * q])), dtype=np.int64)
L = vals[0::2]
R = vals[1::2]
Ns = np.concatenate([L - 1, R])
small = []
for x in range(1, T + 1):
    ys = set()
    for p in range(m):
        v = x
        ys.add(v)
        for j in range(1, m + 1):
            ch = s[(p + j - 1) % m]
            if ch == 'A':
                v -= 1
                if v < 1:
                    break
            elif ch == 'B':
                v = 2 * v
            else:
                v = 2 * v + 1
            if v > 2 * 10 ** 18:
                break
            ys.add(v)
    small.extend(ys)
smallarr = np.array(sorted(small), dtype=np.int64)
maps = set()
for p in range(m):
    k, c = 0, 0
    maps.add((k, c))
    for j in range(1, m + 1):
        ch = s[(p + j - 1) % m]
        if ch == 'A':
            c -= 1
        elif ch == 'B':
            k += 1
            c = 2 * c
        else:
            k += 1
            c = 2 * c + 1
        maps.add((k, c))

by_k = {}
for k, c in maps:
    by_k.setdefault(k, []).append(c)

groups = []
for k, cs in by_k.items():
    chis = [c >> k for c in cs]
    clos = sorted(c - (ch << k) for c, ch in zip(cs, chis))
    groups.append((k, cs, np.array(clos, dtype=np.int64),
                   sum(chis), min(chis), max(chis)))
res = np.searchsorted(smallarr, Ns, side='right').astype(np.int64) % mod
for k, cs, clo, sumchi, minchi, maxchi in groups:
    hi = Ns >> k
    r = Ns & ((1 << k) - 1)
    cnt = len(cs)
    skip = (hi - minchi - T) <= 0
    full = (hi - maxchi - 1 - T) >= 0
    partial = ~skip & ~full
    if full.any():
        idx = np.nonzero(full)[0]
        h = hi[idx]
        gt = cnt - np.searchsorted(clo, r[idx], side='right')
        contrib = ((h - T) % mod) * cnt - sumchi - gt
        res[idx] = (res[idx] + contrib) % mod
    if partial.any():
        idx = np.nonzero(partial)[0]
        n_sub = Ns[idx]
        acc = np.zeros(len(idx), dtype=np.int64)
        for c in cs:
            v = ((n_sub - c) >> k) - T
            v = np.maximum(v, 0)
            acc = (acc + v % mod) % mod
        res[idx] = (res[idx] + acc) % mod
FL = res[:q]
FR = res[q:]
ans = (FR - FL) % mod
sys.stdout.write("\n".join(map(str, ans.tolist())) + "\n")