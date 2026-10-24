n = int(input())
a = list(map(int, input().split()))
k = int(input())
for i in range(k):
    b = list(map(int, input().split()))
    ans = -1
    for s in range(n):
        ok = True
        for i in range(n):
            if a[i] != 0 and b[(i + s) % n] != a[i]:
                ok = False
                break
        if ok:
            ans = s
            break
    print(ans)
