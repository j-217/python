import re


def decodeBits(bits):
    bits.strip('0')
    one_lst = re.findall(r'1+', bits)
    zero_lst = re.findall(r'0+', bits)
    unit = min(min(map(len, zero_lst)), min(map(len, one_lst))) if one_lst and zero_lst else\
        min(map(len, zero_lst)) if not one_lst else min(map(len, one_lst))
    bits = bits.replace('1' * unit * 3, '-').replace('1' * unit, '.').replace(
        '0' * unit * 7, '  ').replace('0' * unit * 3, ' ').replace('0' * unit, '')
    return bits


def decodeMorse(morseCode):
    lst = morseCode.split(' ')
    s_code = ''
    for m_code in lst:
        if m_code:
            s_code += MORSE_CODE[m_code]
        else:
            s_code += ' '
    return re.sub(r'\s+', ' ', s_code).strip()


bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
# decodeBits(bits)
# decodeBits('000000011100000')
decodeBits('011101')


# def decodeBits(bits):
#     import re

#     # remove trailing and leading 0's
#     bits = bits.strip('0')

#     # find the least amount of occurrences of either a 0 or 1, and that is the time hop
#     time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))

#     # hop through the bits and translate to morse
#     return bits[::time_unit].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

# def decodeMorse(morseCode):
#     return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))
