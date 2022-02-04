x = input()
c = 0
while x != "Final del archivo":
    if x > "0":
        x = input()
        if x == "Final del archivo":
            break
        elif x == "0":
            x = input()
            if x == "Final del archivo":
                break
            elif x < "0":
                c = c + 1
    elif x == "Final del archivo":
        break
    else:
        x = input()
print(c)

