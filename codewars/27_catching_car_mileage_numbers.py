def is_interesting(number, awesome_phrases):
    if number < 98:
        print("0_1")
        return 0
    n = number
    possible_num_lst = [n + 1, n + 2]
    if any([is_in_awesome_phrases(n, awesome_phrases), is_follow_by_zero(n), is_same_number(n), is_increment_number(n), \
           is_decrement_number(n), is_palindrome(n)]):
        print("2")
        return 2
    print("*"*10)
    for pos_n in possible_num_lst:
        if any([is_in_awesome_phrases(pos_n, awesome_phrases), is_follow_by_zero(pos_n), is_same_number(pos_n), \
                 is_increment_number(pos_n), is_decrement_number(pos_n), is_palindrome(pos_n)]):
            print("1")
            return 1
    print("*"*10)
    print("0_2")
    return 0


def is_in_awesome_phrases(n, awsome_phrases):
    if n >= 100:
        if n in awsome_phrases:
            print("a1")
            return True
        else:
            print("a2")
            return False

def is_follow_by_zero(n):
    if n >= 100:
        if n % 10**(len(str(n))-1) == 0:
            print("b1")
            return True
        else:
            print("b2")
            return False

def is_same_number(n):
    if n >= 100:
        if len(set([i for i in str(n)])) == 1:
            print("c1")
            return True
        else:
            print("c2")
            return False

def is_increment_number(n):
    if n >= 100:
        incre_str = "1234567890"
        if str(n) in incre_str:
            print("d1")
            return True
        else:
            print("d2")
            return False

def is_decrement_number(n):
    if n >= 100:
        decre_str = "9876543210"
        if str(n) in decre_str:
            print("e1")
            return True
        else:
            print("e2")
            return False

def is_palindrome(n):
    if n >= 100:
        n_lst = [i for i in str(n)]
        n_lst_cp = n_lst.copy()
        n_lst_cp.reverse()
        if n_lst == n_lst_cp:
            print("f1")
            return True
        else:
            print("f2")
            return False

# is_interesting(11208,[1337, 256])
is_interesting(98, [1337.256])