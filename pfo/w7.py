import sys
import numpy as np


def imdying():  # организаторы если читаете, то можете мне по блату выдать 1 место пж
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    v = int(data[1])
    a = np.array(list(map(int, data[2:2 + n])), dtype=np.int64)

    if v == 0:
        nz = (a != 0)
        total = n * (n + 1) // 2
        run = 0
        for x in nz.tolist():
            if x:
                run += 1
            else:
                total -= run * (run + 1) // 2
                run = 0
        total -= run * (run + 1) // 2
        print(total)
        return

    av = abs(v)
    t = 1 if v < 0 else 0
    neg = (a < 0).astype(np.int64)
    par = np.zeros(n + 1, dtype=np.int64)
    par[1:] = np.cumsum(neg) & 1
    c = np.zeros(n + 2, dtype=np.int64)
    c[1:] = np.cumsum(par)
    absa = np.abs(a)
    special = absa != 1
    arr = np.full(n + 2, n, dtype=np.int64)
    arr[:n] = np.where(special, np.arange(n, dtype=np.int64), n)
    nxt = np.minimum.accumulate(arr[::-1])[::-1].copy()
    absp = np.ones(n + 2, dtype=np.int64)
    absp[:n] = absa

    def count(lo, hi, w):
        A = lo + 1
        B = hi + 1
        ones = c[B + 1] - c[A]
        return int(np.where(w == 1, ones, (B - A + 1) - ones).sum())

    l = np.nonzero(a != 0)[0].astype(np.int64)
    w = t ^ par[l]
    cur = l.copy()
    P = np.ones(len(l), dtype=np.int64)
    ans = 0

    if av == 1:
        e = nxt[l] - 1
        ans += count(l, e, w)

    while len(cur):
        j = nxt[cur]
        jc = np.minimum(j, n)
        aj = absp[jc]
        valid = (j < n) & (aj != 0)
        aj_safe = np.maximum(aj, 1)
        valid &= (P <= av // aj_safe)
        if not valid.any():
            break
        j = j[valid]
        aj = aj[valid]
        w = w[valid]
        P = P[valid] * aj
        e = nxt[j + 1] - 1
        m = P == av
        if m.any():
            ans += count(j[m], e[m], w[m])
        cur = j + 1

    print(ans)


imdying()
