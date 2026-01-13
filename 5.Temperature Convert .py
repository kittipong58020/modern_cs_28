def c_to_f(c):
    f = float(c) * 9 / 5 + 32
    return f

inp = input("Celsius : ")
print("Fahrenheit = ",c_to_f(inp))
