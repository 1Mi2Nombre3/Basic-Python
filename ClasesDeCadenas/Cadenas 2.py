c1=input()
read = len(c1)
c2=""
c3=""
for i in range(read):
    if 'A' == c1[i] or 'E' == c1[i] or 'I' == c1[i] or 'O' == c1[i] or 'U' == c1[i]:
        c2 = c2+ c1[i]
    else:
        if c1[i] == " ":
            c3=c3+"_"
        else:
            c3 = c3 + c1[i]
print(c2)
print(c3)