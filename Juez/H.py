T=int(input())
for i in range(T):
    S,R=input().split()
    if S == "Spock" and R == "Tijeras":
        print("Fanatico#1")
    if S == "Spock" and R== "Roca":
        print("Fanatico#1")
    if S=="Tijeras" and R=="Spock":
        print("Fanatico#2")
    if S=="Roca" and R=="Spock":
        print("Fanatico#2")
    if S == "Spock" and R=="Spock":
        print("Empate")

    if S=="Tijeras" and R== "Papel":
        print("Fanatico#1")
    if S == "Tijeras" and R == "Rata":
        print("Fanatico#1")
    if S=="Papel" and R=="Tijeras":
        print("Fanatico#2")
    if S=="Rata" and R=="Tijeras":
        print("Fanatico#2")
    if S=="Tijeras" and R=="Tijeras":
        print("Empate")

    if S=="Papel" and R=="Roca":
        print("Fanatico#1")
    if S=="Papel" and R=="Spock":
        print("Fanatico#1")
    if S=="Roca" and R=="Papel":
        print("Fanatico#2")
    if S=="Spock" and R=="Papel":
        print("Fanatico#2")
    if S=="Papel" and R=="Papel":
        print("Empate")

    if S=="Roca" and R=="Tijeras":
        print("Fanatico#1")
    if S=="Roca" and R=="Rata":
        print("Fanatico#1")
    if S=="Tijeras" and R=="Roca":
        print("Fanatico#2")
    if S=="Rata" and R=="Roca":
        print("Fanatico#2")
    if S=="Roca" and R=="Roca":
        print("Empate")

    if S=="Rata" and R=="Papel":
        print("Fanatico#1")
    if S=="Rata" and R=="Spock":
        print("Fanatico#1")
    if S=="Papel" and R=="Rata":
        print("Fanatico#2")
    if S=="Spock" and R=="Rata":
        print("Fanatico#2")
    if S=="Rata" and R=="Rata":
        print("Empate")
