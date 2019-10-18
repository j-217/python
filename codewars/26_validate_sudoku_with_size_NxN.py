from math import sqrt


class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        for r in self.data:
            for c in r:
                if type(c) is int:
                    continue
                else:
                    return False
        row_num = len(self.data)
        col_num = len(max(self.data))
        if row_num != col_num:
            print("{}x{} (invalin dimension)".format(row_num, col_num))
            return False
        if row_num == col_num and sqrt(row_num).is_integer():
            n = row_num
            valid_set = set(range(1, n+1))
            for row in self.data:
                if set(row) == valid_set:
                    continue
                else:
                    print("Values in wrong order")
                    return False
            for r in range(n):
                col = []
                for c in range(n):
                    col.append(self.data[c][r])
                if set(col) == valid_set:
                    continue
                else:
                    print("Values in wrong order")
                    return False
            for x in range(0, n - int(sqrt(n)) + 1, int(sqrt(n))):
                for y in range(0, n - int(sqrt(n)) + 1, int(sqrt(n))):
                    block = []
                    i = 0
                    while i < int(sqrt(n)):
                        block += self.data[x + i][y: y+int(sqrt(n))]
                        i += 1
                    if set(block) == valid_set:
                        continue
                    else:
                        print("Values in wrong order")
                        return False
            print("Testing valid {}x{}".format(n, n))
            return True

#
# sudoki = Sudoku([
#   [1,2,3,4,5],
#   [1,2,3,4],
#   [1,2,3,4],
#   [1]
# ])
#
# sudoki.is_valid()

sudoki1 = Sudoku([[1, 4, 4, 3, 'a'], [3, 2, 4, 1], [4, 1, 3, 3], [2, 0, 1, 4], ['', False, None, '4']])

sudoki1.is_valid()