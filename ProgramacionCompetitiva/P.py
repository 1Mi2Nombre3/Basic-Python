alp = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"  # 27
n = int(input())
for i in range(n):
    cad = input()
    cad2 = ""
    c = 0
    aux = 0
    for j in cad:
        for k in cad:
            if j == k:
                c = c + 1
        if aux < c:
            aux = c
        c = 0
    cad2 = cad2 + alp[aux - 1]
    for li in cad:
        a = alp.find(li)
        a = ((a + 1) % 27) + aux
        cad2 = cad2 + alp[a - 1]
    print(cad2)
