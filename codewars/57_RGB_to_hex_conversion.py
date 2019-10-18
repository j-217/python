def rgb(r, g, b):
    def check(x):
        # if x < 0:
        #     return 0
        # elif x > 255:
        #     return 255
        # return x
        return 0 if x < 0 else 255 if x > 255 else x
    print('{:0>2X}{:0>2X}{:0>2X}'.format(check(r), check(g), check(b)))

rgb(1,2,3)