def no_dups(s):
    # Your code here
    output = []
    seen = set()
    for i in s.split():
        if i not in seen:
            output.append(i)
            seen.add(i)
    return ' '.join(output)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
