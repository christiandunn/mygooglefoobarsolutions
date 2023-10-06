from fractions import Fraction, gcd
def level3part1(m):
    orig_terminal_indices = []
    orig_normal_rows = []
    N = len(m)
    for i in range(N):
        if sum(m[i]) == 0:
            orig_terminal_indices.append(i)
            #m[i][i] = 1
        else:
            orig_normal_rows.append(i)
            denom = sum(m[i])
            for j in range(N):
                m[i][j] = Fraction(m[i][j], denom)
    orig_to_new_mapping = dict()
    new_row = 0
    new_m = []
    # Rewriting the matrix so that rows with all zeroes are at the bottom
    while new_row < len(orig_normal_rows):
        new_m.append(m[orig_normal_rows[new_row]])
        orig_to_new_mapping[orig_normal_rows[new_row]] = new_row
        new_row += 1
    while new_row < N:
        new_m.append(m[orig_terminal_indices[new_row - len(orig_normal_rows)]])
        orig_to_new_mapping[orig_terminal_indices[new_row - len(orig_normal_rows)]] = new_row
        new_row += 1
    r = 0
    while r < N:
        new_row = [0] * N
        c = 0
        while c < N:
            new_row[orig_to_new_mapping[c]] = new_m[r][c]
            c += 1
        new_m[r] = new_row
        r += 1
    m = new_m
    terminal_indices = list(range(len(orig_normal_rows), N))
    # Create Markov Chain Absorption Probability Matrices for each terminal index
    AA = [[[(m[row][col]-1 if col==row and row not in terminal_indices else m[row][col]) for col in range(N)] for row in range(N)] for _ in terminal_indices]
    BB = [[(1 if row == ti else 0) for row in range(N)] for ti in terminal_indices]
    # A[terminal_index][row][col]
    # B[terminal_index][row]
    # Gaussian Elimination - Linear Algebra way to solve system of equations
    for i, ti in enumerate(terminal_indices):
        A = AA[i]
        B = BB[i]
        for c in range(N):
            if c in terminal_indices:
                continue
            for r in range(c+1, N):
                if r in terminal_indices:
                    continue
                if A[r][c] == 0 or A[c][c] == 0:
                    continue
                factor = -A[r][c]/A[c][c]
                B[r] += factor * B[c]
                for c2 in range(c, N):
                    A[r][c2] += factor * A[c][c2]
        for r in range(N - 1, -1, -1):
            if r in terminal_indices:
                continue
            csum = 0
            for c in range(r+1, N):
                if A[r][r] == 0:
                    continue
                csum += B[c] * A[r][c] / (-A[r][r])
            B[r] = csum
    fractions = []
    for i in range(len(terminal_indices)):
        fractions.append(BB[i][0])
    results = []
    lcm = int(fractions[0].denominator)
    for i in range(1, len(fractions)):
        lcm = lcm * int(fractions[i].denominator) / gcd(lcm, int(fractions[i].denominator))
    for fraction in fractions:
        numerator = int(fraction.numerator)
        if fraction.denominator < lcm:
            numerator = numerator * (lcm / int(fraction.denominator))
        results.append(numerator)
    results.append(int(lcm))
    return results
