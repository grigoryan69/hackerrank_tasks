def ginorts(c):
    code = 0
    if c.isupper():
        code = 10 ** 3
    elif c.isdigit():
        code = 10 ** 6
        if ord(c) % 2 == 0:
            code = 10 ** 9
    return code + ord(c)

if __name__ == '__main__':
    print(*sorted(input(), key=lambda c: ginorts(c)), sep='')