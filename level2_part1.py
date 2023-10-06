def level2part1(x, y):
    # formula: (x,1) = (1/2)x^2 + (1/2)x
    # formula: (x,y) = 
    #   n = x + y - 1
    #   (x,y) = (1/2)n^2 + (1/2)n - (y-1)
    n = x + y - 1
    result = 0.5 * n ** 2 + 0.5 * n - (y - 1)
    return result
