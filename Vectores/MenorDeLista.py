def Men(a):
    aux = a[0]
    for i in a:
        if i <= aux:
            aux = i
    return aux