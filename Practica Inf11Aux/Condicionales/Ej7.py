a,b,c,d,e = map(int,input("5 numbers: ").split())

may = a

if b > may:
    may = b
if c > may:
    may = c
if d > may:
    may = d
if e > may:
    may = e

print("el mayor es ",may)
