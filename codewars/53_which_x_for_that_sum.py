from math import sqrt, fabs


def solve(m):
    # the limit of U is x/(1-x)^2 goes to m = x/(1-x)^2, thus mx^2-(2m+1)x+m = 0,\
    # then we can use x=(-b +/- (b^2-4ac)^0.5)/2m to get the solution.
    m = int(m)
    s = sqrt(fabs((2*m+1)**2 - 4*m**2))
    if m != 0:
        return ((2*m+1)+s)/(2*m) if 0 < ((2*m+1)+s)/(2*m) < 1 else ((2*m+1)-s)/(2*m)

solve(2.00)