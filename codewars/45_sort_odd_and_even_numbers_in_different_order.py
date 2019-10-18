def sort_array(a):
    if a:
        odd_list = []
        even_list = []
        for n in a:
            if n % 2 == 0:
                even_list.append(n)
            else:
                odd_list.append(n)
        # descending odd numbers
        even_list.sort()
        odd_list.sort(reverse=True)
        for index, n in enumerate(a):
            if n % 2 == 0:
                a[index] = even_list.pop()
            else:
                a[index] = odd_list.pop()
        return a
    else:
        return a
