from math import sqrt, ceil

def list_squared(m, n):
	lst = []
	for num in range(m, n+1):
		sums = sum(map(lambda x: x*x, divisors(num)))
		if sqrt(sums).is_integer():
			lst.append([num, int(sums)])
	print(lst)
	return lst


def divisors(num):
	divisors_set = set()
	for i in range(1, ceil(sqrt(num)) + 1):
		if num % i == 0:
			divisors_set.add(i)
			divisors_set.add(int(num/i))
	print(divisors_set)
	return divisors_set


list_squared(1, 1)
