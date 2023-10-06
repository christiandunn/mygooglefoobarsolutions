import math
import itertools

def choose(n, r):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

def level4part1(num_buns, num_required):
    n = num_buns
    r = num_required
    if r > n:
        return []
    if r == n:
        return [[i] for i in range(n)]
    if r == 1:
        return [[0] for _ in range(n)]
    combs = list(reversed(sorted(itertools.combinations(list(range(n)), r - 1))))
    results = [[] for _ in range(n)]
    for i, comb in enumerate(combs):
        for bun in range(n):
            if bun not in comb:
                results[bun].append(i)
    return results


def validate_ans_level4part1(n, r, ans):
    max_key = max(max(sublist) for sublist in ans)
    def find_all_keys_comb_of_req_size(i, want_match):
        bun_combs = itertools.combinations(range(n), i)
        for bun_comb in bun_combs:
            keys_accounted_for = [0 for _ in range(max_key+1)]
            for b in bun_comb:
                for j in ans[b]:
                    keys_accounted_for[j] = 1
            if sum(keys_accounted_for) == max_key + 1:
                if not want_match:
                    print(bun_comb)
                    return True
            else:
                if want_match:
                    print(bun_comb)
                    return False
        return True if want_match else False
    for i in range(1, r):
        if find_all_keys_comb_of_req_size(i, False):
            print("Fail at size ", i)
    if not find_all_keys_comb_of_req_size(r, True):
        print("Fail at size ", r)
