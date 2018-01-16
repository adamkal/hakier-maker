"""Implements FizzBuzz algorithm

https://en.wikipedia.org/wiki/Fizz_buzz
"""


def fizzbuzz_maciek(i):
    """FizzBuzz algorithm"""
    """    if i==0 : wynik="FizzBuzz"
    if  not i % 3:
        wynik="Fizz"
    elif not i % 5:
        wynik="Buzz"  """

    if not  ((i % 3) or (i % 5)):
        wynik="FizzBuzz"
    elif not (i % 3):
        wynik="Fizz"
    elif not (i % 5):
        wynik="Buzz"
    else: wynik=str(i)
#        dupa dupa dupa

    return wynik

def fizzbuzz_kalin(i):
    ret = ""
    if not i % 3:
        ret += "Fizz"
    if not i % 5:
        ret += "Buzz"

    if ret:
        return ret
    return str(i)

def fizzbuzz_diana(i):
    return None

duoa = input("Jak")

fizzbuzz = {
    "kalin": fizzbuzz_kalin,
    "maciek": fizzbuzz_maciek,
    "diana": fizzbuzz_diana,
}[duoa]

assert fizzbuzz['maciek'] == fizzbuzz_maciek

# 0: FizzBuzz
# 1: 1
# 2: 2
# 3: Fizz
# 4: 4
# 5: Buzz
# 6: Fizz
# 7: 7
# 8: 8
# 9: Fizz
# 10: 10
# 11: 11
# 12: FizzBuzz

#
# x, y = 1, 2
#
# t, f = True, False
#
# if (x < y and y>3) and (x*y>2):
#     print(y)
# elif x > y:
#     print(x)
#     if y > 3:
#         if x < 5:
# else:
#     print("Dupa")
