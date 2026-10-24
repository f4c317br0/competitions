import math

def asd():
    try:
        W, H, r = map(float, input().split())
    except:
        return

    if 2 * r > W or 2 * r > H:
        print(0)
        return

    ans_sq = math.floor(W / (2 * r)) * math.floor(H / (2 * r))

    ny1 = 1 + math.floor((H - 2 * r) / (r * math.sqrt(3)))
    n_odd1 = math.floor(W / (2 * r))
    n_even1 = math.floor((W - r) / (2 * r))
    ans_hex1 = (math.ceil(ny1 / 2) * n_odd1) + (math.floor(ny1 / 2) * n_even1)

    ny2 = 1 + math.floor((W - 2 * r) / (r * math.sqrt(3)))
    n_odd2 = math.floor(H / (2 * r))
    n_even2 = math.floor((H - r) / (2 * r))
    ans_hex2 = (math.ceil(ny2 / 2) * n_odd2) + (math.floor(ny2 / 2) * n_even2)

    print(max(ans_sq, ans_hex1, ans_hex2))

asd()
