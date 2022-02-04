n = int(input())
for i in range(n):
    d, m, a = map(int, input().split())
    cv = 0
    aux = 0
    DiasNoBis = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    DiasBis = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a % 400 == 0:
        if m <= 12:
            if m == 1:
                aux = DiasBis[m + 1]
            else:
                aux = DiasBis[m - 1]
        else:
            cv = 1
        if aux != 0:
            for i in range(1, aux + 1):
                if i == d:
                    cv = 0
                    break
                else:
                    cv = 1
        else:
            cv = 1
        if cv == 0:
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")

    elif a % 100 == 0:
        if m <= 12:
            if m == 1:
                aux = DiasNoBis[m + 1]
            else:
                aux = DiasNoBis[m - 1]
        else:
            cv = 1
        if aux != 0:
            for j in range(1, aux + 1):
                if j == d:
                    cv = 0
                    break
                else:
                    cv = 1
        else:
            cv = 1

        if cv == 0:
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
    elif a % 4 == 0:
        if m <= 12:
            if m == 1:
                aux = DiasBis[m + 1]
            else:
                aux = DiasBis[m - 1]
        else:
            cv = 1
        if aux != 0:
            for i in range(1, aux + 1):
                if i == d:
                    cv = 0
                    break
                else:
                    cv = 1
        else:
            cv = 1
        if cv == 0:
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
    else:
        if m <= 12:
            if m == 1:
                aux = DiasNoBis[m + 1]
            else:
                aux = DiasNoBis[m - 1]
        else:
            cv = 1
        if aux != 0:
            for j in range(1, aux + 1):
                if j == d:
                    cv = 0
                    break
                else:
                    cv = 1
        else:
            cv = 1
        if cv == 0:
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
