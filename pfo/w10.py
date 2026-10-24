n, k = map(int, input().split())
a = list(map(int, input().split()))
best = 0
for p in range(1, 101):
    best = max(best, p * sum(min(k, x // p) for x in a))
print(best)