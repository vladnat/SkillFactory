n = 513


def to_2(num):
    s = ''
    while num:
        k = num % 2
        s += str(k)
        num = num // 2
    return s

print(to_2(n)[::-1])
