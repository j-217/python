def mix(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    letters = set(s1) | set(s2)
    lst = []
    for letter in letters:
        if letter.islower():
            n1 = s1.count(letter)
            n2 = s2.count(letter)
            if n1 > 1 or n2 > 1:
                if n1 > n2:
                    lst.append(['1', letter * n1])
                elif n1 == n2:
                    lst.append(['=', letter * n1])
                else:
                    lst.append(['2', letter * n2])
    return '/'.join(map(lambda x: '{}:{}'.format(x[0], x[1]), sorted(lst, key=lambda x: (-len(x[1]), x[0], x[1][0])))) \
            if lst else ''


s1 = "looping is fun but dangerous"
s2 = "less dangerous than coding"
mix(s1, s2)