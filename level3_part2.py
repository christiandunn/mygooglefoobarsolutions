def level3part2(x,y):
    x, y = int(x), int(y)
    not_possible = "impossible"
    if x <= 0 or y <= 0:
        return not_possible
    generations = 0
    while x > 1 or y > 1:
        if x > y:
            factor = max(1, int(x/y) - 1)
            x = x - y * factor
            generations += factor
        elif y > x:
            factor = max(1, int(y/x) - 1)
            y = y - x * factor
            generations += factor
        else:
            return not_possible
    return str(int(generations))
