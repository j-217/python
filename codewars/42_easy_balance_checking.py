# def balance(book):
#     for i in '\"\'~!@#$%^&*():;<>/?\\=,{}[]':
#         book = book.replace(i, ' ')
#     lst = book.split('\n')
#     strng = 'Original Balance: {}\r\n'.format(lst[0].strip())
#     remain = float(lst[0])
#     trim_lst = []
#     total_exp = 0
#     for line in lst[1:]:
#         if line:
#             trim_str = ' '.join(line.split())
#             expense = float(trim_str.split(' ')[-1])
#             total_exp += expense
#             remain -= expense
#             trim_lst.append(' '.join(trim_str.split()[:-1]) + ' {:.2f}'.format(expense) + ' Balance {:.2f}'.format(remain))
#     trim_data = '\r\n'.join(trim_lst)
#     print(strng + trim_data + '\r\n' + 'Total expense  {:.2f}\r\n'.format(total_exp) + 'Average expense  {:.2f}'\
#         .format(total_exp/len(trim_lst)))
import re


def balance(book):
    pattern = re.compile(r'[^a-zA-Z0-9. \n]')
    trim_book_lst = re.sub(pattern, '', book).split('\n')
    # print(trim_book_lst)
    data = ''
    total_exp = 0
    o_balance = remain = float(trim_book_lst[0])
    n = 0
    for line in trim_book_lst[1:]:
        if line:
            expense = float(line.split()[-1])
            total_exp += expense
            remain -= expense
            n += 1
            data += ' '.join(line.split()[:-1]) + ' {:.2f} '.format(expense) + 'Balance {:.2f}\r\n'.format(remain)
    print('Original Balance: {:.2f}\r\n'.format(o_balance) + data + 'Total expense  {:.2f}\r\n'.format(total_exp) + \
           'Average expense  {:.2f}'.format(total_exp/n))


b1 = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.00
"""

b2="""1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tyres;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;"""
balance(b2)



