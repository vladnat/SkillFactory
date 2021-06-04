a = [-67, 76, -94, 59]

n = len(a)
i = 0
while len(a[:(n - i)]) != 0:
    tmp = min(a[:(n - i)])
    a.pop(a.index(tmp))
    a.append(tmp)
    i += 1

print(a)