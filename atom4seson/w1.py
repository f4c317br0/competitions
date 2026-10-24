import math


def zxc(line):
    m, n, q = line
    common_divisor = math.gcd(m, n)
    n //= common_divisor

    if n == 1:
        return 'Yes'
    i = 2
    tempn = n
    while i * i <= tempn:
        if tempn % i == 0:
            if q % i != 0:
                return 'No'
            while tempn % i == 0:
                tempn //= i
        i += 1
    if tempn > 1:
        if q % tempn != 0:
            return 'No'

    return 'Yes'


print(zxc(map(int, input().split())))
