import re


def decodeMorse(morse_code):
    lst = morse_code.split(' ')
    s_code = ''
    for m_code in lst:
        if m_code:
            s_code += MORSE_CODE[m_code]
        else:
            s_code += ' '
    return re.sub(r'\s+', ' ', s_code).strip()
