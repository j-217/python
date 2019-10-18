def generate_hashtag(s):
    str = "".join(s).title().replace(" ", "")
    if 0 < len(str) < 140:
        print("#" + str)
    else:
        print("false")

generate_hashtag("Codewars      ")
generate_hashtag('Codewars Is Nice')
generate_hashtag("i c n")