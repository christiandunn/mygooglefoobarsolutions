def level2part2(n, b):
    # n = number (string)
    # b = base of number (int)
    k = len(n)
    current = n
    seen1 = set([current])
    seen2 = set()
    i = 0
    while True and i < 100:
        i += 1
        y = sorted(list(current))
        x = list(reversed(y))
        yn = 0
        xn = 0
        for i in range(0, k):
            yn = yn * b + int(y[i])
            xn = xn * b + int(x[i])
        zn = xn - yn
        z = []
        for i in range(k-1, -1, -1):
            digit = zn // (b ** i)
            z.append(str(digit))
            zn -= digit * b ** i
        zs = ''.join(z)
        current = zs
        if not seen2:
            if current not in seen1:
                seen1.add(current)
            else:
                seen2.add(current)
        else:
            if current not in seen2:
                seen2.add(current)
            else:
                break
    return len(seen2)
