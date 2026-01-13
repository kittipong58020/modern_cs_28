def INTEGER(n):
    if int(n) % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


inp = input("Integer : ")
print("=",INTEGER(inp))
