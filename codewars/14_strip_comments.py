import re

def solution(string, markers):
    if markers:
        marker_str = ''.join(markers)
        if "^" in marker_str:
            marker_str = marker_str.replace("^", "\^")
        if "-" in marker_str:
            marker_str = marker_str.replace("-", "") + "-"
        # if marker_str.startswith("^") and len(marker_str) == 2:
        #     marker_str = marker_str.replace("^", "") + "^"
        pattern = re.compile(r"[ ]*[{}].*".format(marker_str))
        # print(pattern)
        str = re.sub(pattern, "", string)
        print(str)
        # return str
    else:
        return string


# solution("apples, pears ? and bananas\ngrapes\nbananas !apples", ["?", "!"])
# solution("a #b\nc\nd $e f g", ["#", "$"])
# solution("apples, pears -^ and bananas\ngrapes\nbananas $apples", ["-", "$"])
# solution('avocados cherries\n# oranges apples\noranges = apples bananas pears strawberries\nstrawberries apples pears', ['@', '-', "'", '.', '^', '!', '#', '='])
# solution("pears cherries\nstrawberries pears\n,\n|apples ' oranges '", ['#', '@', '?', '-', '!'])
# solution('apples watermelons avocados apples cherries apples\napples\n-', ['^', '=', '-'])
# solution('strawberries\ncherries apples avocados avocados bananas strawberries\n@ oranges lemons strawberries bananas pears\nbananas\nbananas oranges watermelons', ['=', '.', '?', '!', "'", '-', '^', '@'])
solution('# cherries\nwatermelons @ cherries bananas cherries watermelons\nbananas apples strawberries avocados avocados', ['-', '^', "'", '#'])