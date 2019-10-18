def going(n):
    s = 0
    frac = 1
    for num in range(1, n+1):
        frac *= num
        s += frac
    return float(str(s/frac)[:8])

going(4)