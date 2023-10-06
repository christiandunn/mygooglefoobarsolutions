import math

def choose(n, r):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def partition(n, i = None, s = 0, p = []):
    if i is None:
        i = n
    if s == n:
        return [list(p)]
    results = []
    for j in range(1, min(i + 1, n - s + 1)):
        p.append(j)
        results.extend(partition(n, j, s + j, p))
        p.pop()
    return results

def elements_of_g(partition):
    result = 1
    n = sum(partition)
    cycle_sizes = dict()
    for cycle_size in partition:
        cycle_sizes[cycle_size] = cycle_sizes.get(cycle_size, 0) + 1
        result = result * choose(n, cycle_size) * math.factorial(cycle_size) / cycle_size
        n -= cycle_size
    for cycle_size in cycle_sizes.keys():
        result = result / math.factorial(cycle_sizes[cycle_size])
    return result

def c_g(part1, part2):
    result = sum([sum([gcd(i, j) for i in part1]) for j in part2])
    return result

def solution(w, h, s):
    G = math.factorial(w) * math.factorial(h)
    result = 0
    for part1 in partition(w):
        for part2 in partition(h):
            e_of_g = elements_of_g(part1) * elements_of_g(part2)
            result += e_of_g * (s ** c_g(part1, part2))
    return str(result / G)

print solution(2,3,4)
