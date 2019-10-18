def spin_words(sentence):
    words_list = sentence.split(" ")
    spin_sentence = ""
    for word in words_list:
        if len(word) >= 5:
            spin_word = "".join(reversed(word))
        else:
            spin_word = word
        spin_sentence += spin_word + " "
    print(spin_sentence.strip())
    # return spin_sentence.strip()


spin_words("Welcome")