def perimeter(n):
    n += 1
    a, b = 1, 1
    sum = 1
    if n == 1:
        # print(sum*4)
        return sum*4
    if n == 2:
        # print((sum + b)*4)
        return (sum + b)*4
    while n > 2:
        sum += b
        a, b = b, a + b
        n -= 1
    # print((sum + b)*4)
    return (sum+b)*4

perimeter(7)
perimeter(5)
# perimeter(1)
# perimeter(0)