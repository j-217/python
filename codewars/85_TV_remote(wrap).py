import re

KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/* "
MAP = {c: (i // 8, i % 8) for i, c in enumerate(KEYBOARD)}


def toggle(m):
    up, end = m.group(1), m.group(2)
    shift = '*' * bool(end)
    return f'*{up.lower()}{shift}{end}'


def tv_remote(words):
    chang_words = re.sub(r'([A-Z][^a-z]*)([a-z]?)', toggle, words)
    start, steps = (0, 0), 0
    for l in chang_words:
        x = min(abs(MAP[l][1] - start[1]), 8 - abs(MAP[l][1] - start[1]))
        y = min(abs(MAP[l][0] - start[0]), 6 - abs(MAP[l][0] - start[0]))
        steps += x + y + 1
        start = MAP[l]
    print(steps)
    return steps


# tv_remote('The Quick Brown Fox Jumps Over A Lazy Dog.')
tv_remote('Pack My Box With Five Dozen Liquor Jugs.')
