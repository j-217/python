import re


def song_decoder(song):
    pattern = re.compile(r"(WUB)+")
    # decode_song = re.sub(pattern, " ", song).strip()
    decode_song = pattern.sub(" ", song).strip()
    # decode_song = re.sub(r"\s+", " ", decode_song)
    print(decode_song)

song_decoder("AWUBBWUBC")
song_decoder("WUBAWUBBWUBCWUB")