import sys

for datos in sys.stdin:
    x, d = map(int, datos.split(" "))
    x = str(x)
    x1 = ""
    x2 = ""
    d = str(d)
    may = 0
    for j in x:
        a = int(j)
        if may < a:
            may = a
    if str(may) != d:
        for i in x:
            if i != d:
                x1 = x1 + i
            else:
                x1 = x1 + str(may)
        print(x1)
    else:
        may1 = 0
        for i in x:
            if i != d:
                x1 = x1 + i
        for j in x1:
            a = int(j)
            if may1 < a:
                may1 = a
        for k in x:
            if k != d:
                x2 = x2 + k
            else:
                x2 = x2 + str(may1)
        print(x2)
