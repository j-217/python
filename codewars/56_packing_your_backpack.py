def pack_bagpack(scores, weights, capacity):
    load = [0] * (capacity + 1)
    for score, weight in zip(scores, weights):
        lst = []
        for w, l in enumerate(load):
            a = max(l, weight <= w and load[w - weight] + score)
            lst.append(a)
        load = lst
        # load = [max(l, weight <= w and load[w - weight] + score) for w, l in enumerate(load)]
        print(load)
    print(load[-1])
    # return load[-1]

# def pack_bagpack(S,W,C) :
#     M = [0] * (1 + C)
#     for F,V in enumerate(S) :
#         M = [max(U, M[T - W[F]] + V if W[F] <= T else 0) for T,U in enumerate(M)]
#         print(M)
#     print(M[-1])
#     return M[-1]


# pack_bagpack([10, 15, 9, 5], [5, 1, 3, 4], 8)
pack_bagpack([20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4], 10)