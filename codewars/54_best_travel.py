from itertools import combinations


def choose_best_sum(t, k, ls):
    p_lst = []
    # for comb in combinations(ls, int(k)):
    #     if sum(comb) <= int(t):
    #         p_lst.append(sum(comb))
    # print(max(p_lst) if p_lst else None)
    print(max((s for s in (sum(comb) for comb in combinations(ls, k)) if s <= t), default=None))


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
choose_best_sum(430, 5, xs)
