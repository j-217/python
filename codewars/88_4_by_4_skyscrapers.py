clue_dict = {0: [0, 0], 1: [0, 1], 2: [0, 2], 3: [0, 3],
             4: [0, 3], 5: [1, 3], 6: [2, 3], 7: [3, 3],
             8: [3, 3], 9: [3, 2], 10: [3, 1], 11: [3, 0],
             12: [3, 0], 13: [2, 0], 14: [1, 0], 15: [0, 0]}


def solve_puzzle(clues):
    ans = [[0 for i in range(4)] for i in range(4)]
    for i, n in enumerate(clues):
        if n == 1:
            ans[clue_dict[i][0]][clue_dict[i][1]] = 4
        elif n == 4:
            ans[clue_dict[i][0]][clue_dict[i][1]] = 1
    print(ans)


clues = (2, 2, 1, 3,
         2, 2, 3, 1,
         1, 2, 2, 3,
         3, 2, 1, 3)

solve_puzzle(clues)
