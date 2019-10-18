def duplicate_count(text):
    text = text.upper()
    checked = []
    for letter in text:
        if letter not in checked and text.count(letter) >=2:
            checked.append(letter)
    return len(checked)