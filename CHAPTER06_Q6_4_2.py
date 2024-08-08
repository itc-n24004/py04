def g_p(a=2):
    while True:
        for i in range(2, a):
            if a % i == 0:
                break
        else:
             yield a
        a += 1

i = g_p()
for c in range(10):
    print(next(i), end=" ")
print("")
