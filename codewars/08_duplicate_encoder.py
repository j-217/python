def duplicate_encoder(word):
    encode_str = ""
    for letter in word.lower():
        if word.lower().count(letter) > 1:
            encode_str += ")"
        elif word.lower().count(letter) == 1:
            encode_str += "("
    print(encode_str)


duplicate_encoder("SUCCESS")
duplicate_encoder("n(wF)kORJ(n)vHI")