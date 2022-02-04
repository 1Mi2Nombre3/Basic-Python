def Center(x):
    x = str(x)
    lon = len(x)
    x1 = ""
    if lon % 2 == 0 or lon == 1:
        x1 = ""
        cv = 0
        while lon >= 3:
            a = lon // 2
            x1 = x1 + x[a - 1]
            x1 = x1 + x[a]
            lon = len(x1)
            cv = 1
        if cv == 1:
            print(x1)
        else:
            print(x)
    else:
        a = lon // 2
        x = x[a]
        print(x)