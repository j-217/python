import ipaddress


def int32_to_ip(int32):
    # string = '{:0>32b}'.format(int32)
    # lst = []
    # for i in range(0, 32, 8):
    #     lst.append(string[i:i+8])
    # print(lst)
    # ip = '.'.join(str(int(ip, 2)) for ip in lst)
    # print(ip)
    print(ipaddress.ip_address(int32))


int32_to_ip(123123)