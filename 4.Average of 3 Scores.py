def average(a, b, c):
    avg = (float(a) + float(b) + float(c)) / 3
    return avg


inp1 = input("Number 1 : ")
inp2 = input("Number 2 : ")
inp3 = input("Number 3 : ")

print(f"Average Score = {average(inp1, inp2, inp3):.2f}")

