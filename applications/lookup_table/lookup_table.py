# Your code here
import random
import math


def slowfun_too_slow(x, y):
    # multiply x by y times, if x = 3 & y = 4, 3^4 or 3 * 3 * 3 * 3
    v = math.pow(x, y)

    # multiply v in decsending order by 1 until we reach, v*(v-1) * (v-2) * (v-3) etc down to 1
    v = math.factorial(v)

    # divide v to get a whole number
    v //= (x + y)

    # divide v by 982451653 to get the remainder
    v %= 982451653

    # return remainder
    return v


stuff = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # i = math.pow(x, y)
    # if i not in stuff:
    #     stuff[i] = slowfun_too_slow(x, y)
    # return stuff[i]

    if (x, y) not in stuff:
        stuff[(x, y)] = slowfun_too_slow(x, y)
    return stuff[(x, y)]


# Do not modify below this line!


for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
