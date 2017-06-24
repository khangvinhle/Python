# base = 10
# exp = 4


# def hello_world():
#     base = 20
#     print('inside the helloworld base is', base)
#     return 'Hello,world'
# print(hello_world())

# def ret_5():
#     print(5)
#
#
# print(ret_5())

# def compute_exp(base, exp):
#     print('inside of function,base is', base)
#     print('inside of function,exp is', exp)
#     return base ** exp
# print('out side of function,base is', base)
# print('out side of function,exp is', exp)
# # test cases
# print(compute_exp(5, 0))
# print(compute_exp(5, 3))
# print(compute_exp(8, 2))

# def is_a_party(apples, pizzas):
#     if apples > 10 and pizzas > 10:
#         return True
#     else:
#         return False
#
#
# def throw_party():
#     num_apples = int(input('how many apples do you have?'))
#     num_pizzas = int(input('how many pizzas do you have?'))
#     if is_a_party(num_apples, num_pizzas):
#         return 'dude let\'s party down!'
#     else:
#         return 'you\'ll have to go to the store first!'
#
#
# # testing functions:
# print(is_a_party(20, 20))
# print(is_a_party(5, 15))
# print(is_a_party(5, 2))
# print(is_a_party(14, 8))
#
# print(throw_party())

def is_vowel(c):
    if c == 'a' or c == 'o' or c == 'e' or c == 'u' or c == 'i':
        return True
    elif c == 'A' or c == 'O' or c == 'E' or c == 'U' or c == 'I':
        return True
    else:
        return False


def only_vowels(phrase):
    voel_string = ''
    for letter in phrase:
        if is_vowel(letter):
            voel_string = voel_string + letter
    return voel_string


# print(is_vowel('l'))
# print('the vowels in the phrase \'tim the beAver\' are:', only_vowels('tim the beAver'))
# print(only_vowels('heLlo WorlD'))
print(only_vowels('klXn'))
