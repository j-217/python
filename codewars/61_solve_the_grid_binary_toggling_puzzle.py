# def find_solution(puzzle):
#     """
#     no need to physically toggle the values,
#     simple list the rows begining with zero
#     and the columns beginning with zero,
#     if the first row was toggled then we need to list the columns which begin with 1
#
#     """
#     # list rows beginning with zero
#     sol = [row for row in range(len(puzzle)) if puzzle[row][0] == 0]
#
#     if len(sol) > 0 and sol[0] == 0:  # check to see if the first row was toggled
#         # if it was then we need to note the postion of the ones
#         sol.extend([i + len(puzzle) for i in range(len(puzzle)) if puzzle[0][i] == 1])
#     else:
#         # else note the position of the zeros
#         sol.extend([i + len(puzzle) for i in range(len(puzzle)) if puzzle[0][i] == 0])
#
#     print(sol)


def find_solution(puzzle):
    col_lst, row_lst = [], []
    # 检查首列每个数，如果与第一个数不同，说明不同数的那行发生改变
    for i, row in enumerate(puzzle):
        if row[0] ^ puzzle[0][0]:
            row_lst.append(i)
    # 检查首行每个数，如果为0，说明该列发生改变
    for i, col in enumerate(puzzle[0]):
        if col == 0:
            col_lst.append(i + len(puzzle))
    return row_lst + col_lst
    # return [j for j, r in enumerate(m) if r[0]^m[0][0]] + [len(m)+i for i,b in enumerate(m[0]) if not b]


puzzle = [[0, 1, 1], [0, 1, 1], [0, 1, 1]]
# puzzle = [[ 1, 0, 0 ], [ 1, 0, 0 ], [ 0, 1, 1 ]]
find_solution(puzzle)