import string
# https://docs.python.org/2/library/string.html#string.punctuation


def word_count(s):

    for char in string.punctuation:
        # remove punucation except for apostrophe
        if char is not "'":
            s = s.replace(char, "")
    counter = {}
    s = s.lower()
    s = s.split()
    for i in s:
        if i not in counter:
            counter[i] = 0
        counter[i] += 1

    return counter


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
