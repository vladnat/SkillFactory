from time import time
time1 = time()
f = False
for a in range(1, int(150 / 4 ** 0.2)):
    qa = a ** 5
    for b in range(a, int(150 / 3 ** 0.2)):
        qab = qa + b ** 5
        for c in range(b, int(150 / 2 ** 0.2)):
            qac = qab + c ** 5
            for d in range(c, 150):
                qad = qac + d ** 5
                e = int(qad ** 0.2)
                if qad == e ** 5:
                    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e, "total =", a + b + c + d + e)
                    f = True
                    break
            if f:
                break
        if f:
            break
    if f:
        break
time2 = time()
print("time:", time2 - time1, "sec.")