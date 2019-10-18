import re
import heapq


def decodeBitsAdvanced(bits):
    bits = bits.strip('0')
    if bits == '':
        return bits
    zero_lst = re.findall(r'0+', bits)
    one_lst = re.findall(r'1+', bits)
    print(heapq.nsmallest(5, map(len, zero_lst)))
    print(heapq.nsmallest(5, map(len, one_lst)))


def decodeMorse(morseCode):
    pass


bits = '0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000'
decodeBitsAdvanced(bits)
