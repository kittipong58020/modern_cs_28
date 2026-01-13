def INTEGER(n):
    n = int(n)
    if n > 0:
        return "POSITIVE"
    elif n < 0:
        return "NEGATIVE"
    else:
        return "ZERO"


inp = input("Integer : ")
print("Output = ",INTEGER(inp))
