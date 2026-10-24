import sys
import numpy as np

mod = 1000000007


def omg():
    data = sys.stdin.buffer.read().split()
    n, L, R = int(data[0]), int(data[1]), int(data[2])
    a = [int(x) for x in data[3:3 + n]]
    adj = [[] for _ in range(n)]
    pos = 3 + n
    for _ in range(n - 1):
        u = int(data[pos]) - 1
        v = int(data[pos + 1]) - 1
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    order = []
    par = [-1] * n
    st = [0]
    while st:
        v = st.pop()
        order.append(v)
        for u in adj[v]:
            if u != par[v]:
                par[u] = v
                st.append(u)
    P = n + 1
    M = np.uint64(mod)
    X = np.arange(P, dtype=np.uint64)
    f = [None] * n
    for v in range(n):
        if a[v] <= R:
            arr = np.zeros((a[v] + 1, P), dtype=np.uint64)
            arr[a[v]] = 1
        else:
            arr = np.zeros((1, P), dtype=np.uint64)
        f[v] = arr
    rootg = None
    for idx in range(n - 1, -1, -1):
        c = order[idx]
        fc = f[c]
        g = fc[L:R + 1].sum(axis=0) % M if L < fc.shape[0] else np.zeros(P, dtype=np.uint64)
        if idx == 0:
            rootg = g
            break
        p = par[c]
        fp = f[p]
        d1 = fp.shape[0] - 1
        d2 = fc.shape[0] - 1
        d = min(R, d1 + d2)
        nw = np.zeros((d + 1, P), dtype=np.uint64)
        cut = g * X % M
        nw[:d1 + 1] = fp * cut % M
        cnt = 0
        if d1 <= d2:
            for i in range(d1 + 1):
                lim = min(d2, R - i)
                if lim < 0:
                    break
                nw[i:i + lim + 1] += fp[i] * fc[:lim + 1]
                cnt += 1
                if cnt == 16:
                    nw %= M
                    cnt = 0
        else:
            for j in range(d2 + 1):
                lim = min(d1, R - j)
                if lim < 0:
                    break
                nw[j:j + lim + 1] += fc[j] * fp[:lim + 1]
                cnt += 1
                if cnt == 16:
                    nw %= M
                    cnt = 0
        nw %= M
        f[p] = nw
        f[c] = None
    y = [int(t) for t in (rootg * X % M)]
    poly = [1]
    for j in range(n + 1):
        new = [0] * (len(poly) + 1)
        for k, val in enumerate(poly):
            new[k + 1] = (new[k + 1] + val) % mod
            new[k] = (new[k] - j * val) % mod
        poly = new
    fact = [1] * (n + 2)
    for i in range(1, n + 2):
        fact[i] = fact[i - 1] * i % mod

    coef = [0] * (n + 1)
    for i in range(n + 1):
        if y[i] == 0:
            continue
        q = [0] * (n + 1)
        q[n] = poly[n + 1]
        for k in range(n, 0, -1):
            q[k - 1] = (poly[k] + i * q[k]) % mod
        den = fact[i] * fact[n - i] % mod
        if (n - i) & 1:
            den = (mod - den) % mod
        sc = y[i] * pow(den, mod - 2, mod) % mod
        for k in range(n + 1):
            coef[k] = (coef[k] + q[k] * sc) % mod

    print(" ".join(map(str, coef[1:])))


omg()
