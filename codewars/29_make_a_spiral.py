def spiralize(size):
    lst = [[1]*size for i in range(size)]
    top = 1
    left = 0
    right = size - 1
    bottom = size - 1
    while left < right and top < bottom:
        # go right
        i = left
        while i < right:
            lst[top][i] = 0
            i += 1
        right -= 1

        # go down
        i = top
        while i < bottom:
            lst[i][right] = 0
            i += 1
        bottom -= 1

        # go left
        i = right
        while i > left:
            lst[bottom][i] = 0
            i -= 1
        left += 1

        # go up
        i = bottom
        while i > top:
            lst[i][left] = 0
            i -= 1
        top += 1

    print(lst)
    return lst


spiralize(5)
spiralize(2)