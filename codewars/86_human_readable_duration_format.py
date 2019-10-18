def format_duration(seconds):
    if seconds == 0:
        return 'now'
    years, left = seconds // 31536000, seconds % 31536000
    days, left = left // 86400, left % 86400
    hours, left = left // 3600, left % 3600
    minutes, left = left // 60, left % 60
    _seconds = left % 60
    lst_sec = [years, days, hours, minutes, _seconds]
    lst_str = ['year', 'day', 'hour', 'minute', 'second']
    lst = []
    for x, y in zip(lst_sec, lst_str):
        if x == 1:
            lst.append(str(x) + ' ' + y)
        elif x > 1:
            lst.append(str(x) + ' ' + y + 's')
    res = ' and '.join(lst)
    n = res.count(' and ')
    return res.replace(' and ', ', ', n - 1) if n > 1 else res


format_duration(3662)
