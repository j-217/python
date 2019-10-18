def compare(s1, s2):
    s1 = s1.split('.')
    s2 = s2.split('.')
    if len(s1) < len(s2):
        for i in range(len(s2)-len(s1)):
            s1.append('0')
    elif len(s1) > len(s2):
        for i in range(len(s1)-len(s2)):
            s2.append('0')
    for i in range(len(s1)):
        if int(s1[i]) == int(s2[i]):
            continue
        if int(s1[i]) > int(s2[i]):
            return 1
        if int(s1[i]) < int(s2[i]):
            return -1
    return 0

compare('1.2.3', '1.02.003')