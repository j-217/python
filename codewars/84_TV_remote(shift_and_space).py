KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/' "


def tv_remote(word):
    start, steps, shifted = [0, 0], 0, 0
    for letter in word:
        if letter.isupper() and shifted == 0:
            coordinate = [KEYBOARD.find("'") // 8, KEYBOARD.find("'") % 8]
            steps += abs(coordinate[0] - start[0]) + \
                abs(coordinate[1] - start[1]) + 1
            start = coordinate
            coordinate = [KEYBOARD.find(
                letter) // 8, KEYBOARD.find(letter) % 8]
            steps += abs(coordinate[0] - start[0]) + \
                abs(coordinate[1] - start[1]) + 1
            start = coordinate
            shifted = 1
        elif letter.isupper() and shifted == 1:
            coordinate = [KEYBOARD.find(
                letter) // 8, KEYBOARD.find(letter) % 8]
            steps += abs(coordinate[0] - start[0]) + \
                abs(coordinate[1] - start[1]) + 1
            start = coordinate
        elif letter.islower() and shifted == 1:
            coordinate = [KEYBOARD.find("'") // 8, KEYBOARD.find("'") % 8]
            steps += abs(coordinate[0] - start[0]) + \
                abs(coordinate[1] - start[1]) + 1
            start = coordinate
            coordinate = [KEYBOARD.find(
                letter) // 8, KEYBOARD.find(letter) % 8]
            steps += abs(coordinate[0] - start[0]) + \
                abs(coordinate[1] - start[1]) + 1
            start = coordinate
            shifted = 0
        else:
            coordinate = [KEYBOARD.find(
                letter) // 8, KEYBOARD.find(letter) % 8]
            steps += abs(coordinate[0] - start[0]) + \
                abs(coordinate[1] - start[1]) + 1
            start = coordinate
    return steps
