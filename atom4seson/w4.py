from math import gcd

a, b, c = map(int, input().split())
if a % 2 == 0 and (a // 2) % gcd(b, c) == 0:
    print("Yes")
else:
    print("No")
