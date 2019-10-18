def Kprime(k, num):
    prime_factors = []
    count = 0
    p = 2
    while p <= num and count < k:
        if num % p == 0:
            prime_factors.append(p)
            num /= p
            count += 1
        else:
            p += 1
    # print(prime_factors if num == 1 and count == k else False)
    return prime_factors if num == 1 and count == k else False


def count_Kprimes(k, start, nd):
    print([num for num in range(start, nd + 1) if Kprime(k, num)])
    # return [num for num in range(start, nd + 1) if Kprime(k, num)]


def puzzle(s):
    count = 0
    one_prime_fac = Kprime(1, s)
    three_prime_fac = Kprime(3, s)
    seven_prime_fac = Kprime(7, s)
    for seven_p in seven_prime_fac:
        for three_p in three_prime_fac:
            if s - seven_p - three_p in one_prime_fac:
                count += 1
    return count


# Kprime(5, 1523403)

# count_Kprimes(2, 1523399, 1523858)
count_Kprimes(2, 0, 100)
