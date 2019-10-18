import re


def change(s, prog, version):
    s_lst = s.split('\n')
    print(s_lst[5].split(':')[-1])
    progrom = 'Program: ' + prog
    author = 'Author: g964'
    phone_pattern = re.compile(r'\+1\-\d{3}\-\d{3}\-\d{4}')
    phone = re.search(phone_pattern, s_lst[3].split(':')[-1])
    print(phone)
    ver_pattern = re.compile(r'^\d+\.\d+$')
    ver = re.search(ver_pattern, s_lst[5].split(': ')[-1])
    print(ver)
    date = 'Date: 2019-01-01 '
    if phone is None or ver is None:
        print('1')
        return 'ERROR: VERSION or PHONE'
    else:
        if s_lst[5].split(': ')[-1] == '2.0':
            final = progrom + ' ' + author + ' ' + 'Phone: +1-503-555-0090' + ' ' + date + s_lst[5]
            print(final)
            return final
        elif s_lst[5].split(': ')[-1] is not '2.0':
            final = progrom + ' ' + author + ' ' + 'Phone: +1-503-555-0090' + ' ' + date + 'Version: ' + version
            print(final)
            return final


s = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-9111\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'
change(s, 'Ladder', '1.1')

