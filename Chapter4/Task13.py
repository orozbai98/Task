from datetime import datetime

count = True

def superDigit(n, k=1):
    n = str(n) * k
    p = 0

    for i in n:
        p += int(i)

    global count

    if count:
        if int(str(p).__len__()) < 2:
            count = False

        p = int(superDigit(p))

    return p


start = datetime.now()
total = superDigit(56558484218879754894)
print(datetime.now() - start)
print(total)